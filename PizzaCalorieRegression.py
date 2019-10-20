
import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import nn,from_numpy, tensor, long, float, optim
from torch.autograd import Variable
import torch.nn.functional as F
from torchvision import datasets, transforms, models
from torch.utils.data import Dataset, DataLoader

from PizzaDataset import PizzaDataset



if __name__ == '__main__':
    dataset = PizzaDataset()
    trainloader = DataLoader(dataset=dataset,
                                batch_size = 32,
                                shuffle=True, num_workers=2,)
    testloader = DataLoader(dataset=dataset,
                                batch_size = 32,
                                shuffle=True, num_workers=2,)
    print('loaded dataset')
    print(testloader)

    device = torch.device("cuda" if torch.cuda.is_available() 
                                  else "cpu")
    model = models.resnet50(pretrained=True)
    print(model)
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
    for epoch in range(EPOCH):
        for step, (batch_x, batch_y) in enumerate(trainloader): # for each training step
            
    #         b_x = Variable(batch_x)
    #         b_y = Variable(batch_y)
            b_x = batch_x
            b_y = batch_y
            prediction = model(b_x).type(float)     # input x and predict based on x
            print(prediction, b_y)
            loss = criterion(prediction, b_y)     # must be (1. nn output, 2. target)
            optimizer.zero_grad()   # clear gradients for next train
            loss.backward()         # backpropagation, compute gradients
            optimizer.step()        # apply gradients
            running_loss += loss.item()
            test_loss = 0
            accuracy = 0
            model.eval()
            train_losses.append(running_loss/len(trainloader))
            print(f"Epoch {epoch+1}/{EPOCH}.. "
                f"Train loss: {running_loss/EPOCH:.3f}.. ")
            running_loss = 0
            model.train()
    torch.save(model, 'pizzamodel.pth')