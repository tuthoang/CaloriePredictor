
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import xlsxwriter
import torch
from torch import nn,from_numpy, tensor, long, float, optim
from torch.autograd import Variable
import torch.nn.functional as F
from torchvision import datasets, transforms, models
from torch.utils.data import Dataset, DataLoader

from PizzaDataset import CustomDataSet

def test_model(PATH):
    start = time.time()
    test_data_dir = "WebScrape/test"
    test_dataset = CustomDataSet(test_data_dir)
    testloader = DataLoader(dataset=test_dataset,
                                shuffle=True)
    print('loaded dataset')
    print(testloader)
    model = torch.load(PATH)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.fc.parameters(), lr=0.003)
    running_loss = 0
    number_images = 0
    # with torch.no_grad():
    #     for data in testloader:
    #         images, labels = data
    #         outputs = model(images)
    #         _, predicted = torch.max(outputs.data, 1)
    #         total += labels.size(0)
    #         correct += (predicted == labels).sum().item()
    test_losses = []
    for step, (data_x, data_y) in enumerate(testloader): # for each training step
        number_images += len(data_y)
        prediction = model(data_x).type(float)     # input x and predict based on x
        print(prediction, data_y)
        loss = criterion(prediction, data_y)     # must be (1. nn output, 2. target)
        optimizer.zero_grad()   # clear gradients for next train
        loss.backward()         # backpropagation, compute gradients
        optimizer.step()        # apply gradients
        running_loss += loss.item()
        model.eval()
        # loss_dataframe.to_excel(writer, f'{epoch}_{step}')
        model.eval()
        test_losses.append(running_loss/number_images)
    print(number_images)
    print(f"Test loss: {running_loss/number_images:.3f}.. ")
    print(f"Elapsed Time: {time.time()-start}")

if __name__ == '__main__':
    PATH = 'pizzamodel.pth'
    test_model(PATH)