import torch.optim as optim

class SGD(optim.SGD):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)