
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlsxwriter
import torch
from torch import nn,from_numpy, tensor, long, float, optim
from torch.autograd import Variable
import torch.nn.functional as F
from torchvision import datasets, transforms, models
from torch.utils.data import Dataset, DataLoader

from PizzaDataset import CustomDataSet



if __name__ == '__main__':
    train_data_dir = "WebScrape/images"
    test_data_dir = "WebScrape/test"
    train_dataset = CustomDataSet(train_data_dir)
    test_dataset = CustomDataSet(test_data_dir)
    trainloader = DataLoader(dataset=train_dataset,
                                batch_size = 32,
                                shuffle=True, num_workers=2,)
    testloader = DataLoader(dataset=test_dataset,
                                batch_size = 32,
                                shuffle=True, num_workers=2,)
    print('loaded dataset')
    print(testloader)

    device = torch.device("cuda" if torch.cuda.is_available() 
                                  else "cpu")
    model = models.resnet50(pretrained=True)
    print(model)
    file1 = open("loss.txt","w") 
    for param in model.parameters():
        param.requires_grad = False
    # nn.Linear(2048, 512),
    #                                  nn.ReLU(),
    #                                  nn.Dropout(0.2),
    #                                  nn.Linear(512, 10),
    #                                  nn.ReLU())
    model.fc = nn.Sequential(
            torch.nn.Linear(2048, 512),
            torch.nn.LeakyReLU(),
            torch.nn.Linear(512, 10),
            torch.nn.LeakyReLU(),
            torch.nn.Linear(10, 1),
            torch.nn.ReLU()
        )
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.fc.parameters(), lr=0.003)
    model.to(device)
    print(trainloader)
    EPOCH = 10
    running_loss = 0
    train_losses, test_losses = [], []
    dataframes = []
    writer = pd.ExcelWriter('loss.xlsx', engine = 'xlsxwriter')
    epoch_steps = []
    for epoch in range(EPOCH):
        running_loss = 0
        number_images = 0
        for step, (batch_x, batch_y) in enumerate(trainloader): # for each training step
            number_images += len(batch_y)
            b_x = batch_x
            b_y = batch_y
            prediction = model(b_x).type(float)     # input x and predict based on x
            print(prediction, b_y, len(trainloader), len(b_y))
            loss = criterion(prediction, b_y)     # must be (1. nn output, 2. target)
            optimizer.zero_grad()   # clear gradients for next train
            loss.backward()         # backpropagation, compute gradients
            optimizer.step()        # apply gradients
            running_loss += loss.item()
            test_loss = 0
            accuracy = 0
            model.eval()
            p = prediction.clone().detach().numpy()
            y = b_y.clone().detach().numpy()

            print(y.shape)
            print(p.shape)
            loss_dataframe = pd.DataFrame({'Actual': y.flatten(), 
                                            'Predicted': p.flatten()})
            dataframes.append(loss_dataframe)
            epoch_steps.append(f'{epoch}_{step}')
            # loss_dataframe.to_excel(writer, f'{epoch}_{step}')
            model.train()
        train_losses.append(running_loss/number_images)
        print(f"Epoch {epoch+1}/{EPOCH}.. "
            f"Train loss: {running_loss/number_images:.3f}.. ")
    for i, dataframe in enumerate(dataframes):
        dataframe.to_excel(writer, sheet_name = epoch_steps[i])

    writer.save()
    writer.close()
    file1.close()
    torch.save(model, 'pizzamodel.pth')
    np.savetxt('loss.csv', train_losses, delimiter=',')
    plt.plot(train_losses)