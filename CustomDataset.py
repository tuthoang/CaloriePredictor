import numpy as np
from torch import nn,from_numpy, tensor, long, float, optim

from torch.utils.data import Dataset, DataLoader
from torch.autograd import Variable
import torch.nn.functional as F
from torchvision import datasets, transforms, models
import torchvision
import json
import matplotlib.pyplot as plt
import matplotlib as mpl
# mpl.rcParams['axes.grid'] = False
# mpl.rcParams['image.interpolation'] = 'nearest'
# mpl.rcParams['figure.figsize'] = 15, 25

with open('calories.json') as json_file:
    calories = json.load(json_file)


# data_dir = "WebScrape/images"
from pathlib import Path
from PIL import Image
import numpy as np

def LoadImages(data_dir):
    x_dataset = []
    y_dataset = []
    for filename in Path(data_dir).glob('**/*.jpg'):
        x_dataset.append(filename)
        food_type = filename.parent.parts[-1] # Last part of directory Name
        y_dataset.append(calories[food_type])
    return x_dataset, y_dataset

class CustomDataSet(Dataset):
    def __init__(self, dataset):
        self.x_data, self.y_data = LoadImages(dataset)
        self.len = len(self.x_data)
        print(self.len)
        # List of Transformations
        self.transform = transforms.Compose([transforms.Resize(224),
                                                transforms.RandomCrop(224),
                                                transforms.RandomAffine([-90,90]),
                                                transforms.ColorJitter(contrast=(0.1, 2.0)),
                                                transforms.RandomVerticalFlip(p=0.5),
                                                transforms.ToTensor()
                                                ])

    def __getitem__(self, index):
        x = self.transform(Image.open(self.x_data[index]))
        y = tensor(self.y_data[index], dtype=float)
        y = y.unsqueeze(0) # Turn tensor into a 1x vector
        return x, y
    
    def __len__(self):
        return self.len

def imshow(inp, title=None):
    """Imshow for Tensor."""
    inp = inp.numpy().transpose((1, 2, 0))
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)  # pause a bit so that plots are updated

if __name__ == '__main__':
    train_data_dir = "WebScrape/test"

    dataset = CustomDataSet(train_data_dir)
    print(dataset)

    testloader = DataLoader(dataset=dataset,
                                batch_size = 32,
                                shuffle=True, num_workers=2,)
    for step, (batch_x, batch_y) in enumerate(testloader): # for each training step
        b_x = batch_x
        b_y = batch_y

        # Plot images to see what they look like. Should have some transformation
        out = torchvision.utils.make_grid(b_x)
        imshow(out, f'Step: {step}')
        plt.show(block=False)
    plt.show()