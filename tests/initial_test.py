import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

import deepsight.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)  # Fully connected layer with 128 neurons
        self.fc2 = nn.Linear(128, 10)       # Fully connected layer with 10 output neurons (for 10 classes)

    def forward(self, x):
        x = x.view(-1, 28 * 28)             # Flatten the input tensor
        x = torch.relu(self.fc1(x))         # Apply ReLU activation
        x = self.fc2(x)                     # Output layer (logits)
        return x

def test1():
    pass