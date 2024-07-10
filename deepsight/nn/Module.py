import torch
import torch.nn as nn
import inspect
from types import MethodType


def copy_class_attributes(source_instance, target_instance):
    # Copy instance attributes
    for attr, value in source_instance.__dict__.items():
        setattr(target_instance, attr, value)

    # Copy class attributes and methods
    for name, member in inspect.getmembers(source_instance.__class__):
        if not name.startswith('__'):
            if inspect.isfunction(member) or inspect.ismethod(member):
                # Bind the function to the target instance
                bound_method = MethodType(member, target_instance)
                setattr(target_instance, name, bound_method)
            else:
                setattr(target_instance.__class__, name, member)

def deep_see(cls):
    """
    Class decorator to create an instance of a different class
    but with the same methods and variables as the original class.
    """
    def decorator(*args, **kwargs):
        # Create an instance of the target class
        source_instance = cls(*args, **kwargs)
        target_instance = Module()
        # Copy attributes and methods
        copy_class_attributes(source_instance, target_instance)
        return target_instance
    return decorator


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

        for name, param in super().named_parameters():
            param.forward = see_param(param.forward, name)