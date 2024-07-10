import torch
import torch.nn as nn



class Linear(nn.Linear):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def forward(self, input: torch.Tensor) -> torch.Tensor:
        print(f"RUNNING LAYER:")
    
        # Call the original function
        result = super().forward(input)
        
        # Code to execute after the function call
        print(f"RESULT:\n{result}")
        
        return result
    
