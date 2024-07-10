import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

import deepsight.nn as ds

class DSSimpleNN(ds.Module):
    def __init__(self):
        super(DSSimpleNN, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)  # Fully connected layer with 128 neurons
        self.fc2 = nn.Linear(128, 10)       # Fully connected layer with 10 output neurons (for 10 classes)

    def forward(self, x):
        x = x.view(-1, 28 * 28)             # Flatten the input tensor
        x = torch.relu(self.fc1(x))         # Apply ReLU activation
        x = self.fc2(x)                     # Output layer (logits)
        return x



def test_using_DS_module():
    class DSSimpleLR(ds.Module):
        def __init__(self, input=4, output=1):
            super(DSSimpleLR, self).__init__()
            self.fc1 = nn.Linear(input, output)

        def forward(self, x):
            return self.fc1(x)

    X = torch.Tensor([[2, 4, 2, 1], [40, 37, -2, 0]]) 
    model = DSSimpleLR()

    expected_result = (X @ model.fc1.weight.T) + model.fc1.bias
    
    assert (expected_result == model(X)).all()


def test_using_NN_decorator():
    @ds.deep_see
    class NNSimpleLR(nn.Module):
        def __init__(self, input=4, output=1):
            super().__init__()
            self.fc1 = nn.Linear(input, output)

        def forward(self, x):
            return self.fc1(x)
        
    X = torch.Tensor([[2, 4, 2, 1], [40, 37, -2, 0]]) 
    model = NNSimpleLR(input=4, output=3)

    expected_result = (X @ model.fc1.weight.T) + model.fc1.bias

    assert (expected_result == model(X)).all()