import torch
import torch.nn as nn


def see_param(forward_func, name):
    """
    Visualize a parameter
    """

    def wrapper(*args, **kwargs):
        print(f"RUNNING LAYER: {name}")
        
        # Call the original function
        result = forward_func(*args, **kwargs)
        
        # Code to execute after the function call
        print(f"RESULT:\n{result}")
        
        return result
    return wrapper

class Module(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)