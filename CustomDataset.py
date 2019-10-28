import numpy
from torch import nn,from_numpy, tensor, long, float, optim
from torch.utils.data import Dataset, DataLoader
from torch.autograd import Variable
import torch.nn.functional as F
from torchvision import datasets, transforms, models
import json

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
        # print(filename)
        # print('---', filename.parent.parts[-1])
        transforms.Compose([transforms.Resize(224),
                                            transforms.RandomCrop(224),
                                        transforms.ToTensor()
                                        ])
#         im = np.asarray(Image.open(filename).convert("RGB"))
        x_dataset.append(filename)
        # im.close()
        pizza_type = filename.parent.parts[-1] # Last part of directory Name
        y_dataset.append(calories[pizza_type])
    return x_dataset, y_dataset

class CustomDataSet(Dataset):
    def __init__(self, dataset):
        self.x_data, self.y_data = LoadImages(dataset)
        self.len = len(self.x_data)
        print(self.len)
        # List of Transformations
        self.transform = transforms.Compose([transforms.Resize(224),
                                                transforms.RandomCrop(224),
                                                transforms.ToTensor()
                                                ])

    def __getitem__(self, index):
        x = self.transform(Image.open(self.x_data[index]))
        y = tensor(self.y_data[index], dtype=float)
        y = y.unsqueeze(0) # Turn tensor into a 1x vector
        return x, y
    
    def __len__(self):
        return self.len

if __name__ == '__main__':
    dataset = PizzaDataset()
    train_loader = DataLoader(dataset=dataset,
                                batch_size = 32,
                                shuffle=True,
                                num_workers=2)