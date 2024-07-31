import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

import deepsight.nn as ds

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
