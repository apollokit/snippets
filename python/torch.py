import torch
import numpy as np

def get_torch_numpy(tensor: torch.Tensor) -> np.ndarray:
    """Get a numpy version of a torch tensor
    
    Args:
        tensor: the input tensor
    
    Returns:
        output as numpy array
    """
    return tensor.cpu().numpy()