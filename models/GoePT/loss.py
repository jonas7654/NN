import numpy as np
from numpy.typing import ArrayLike

eps = 1e-6

def cross_entropy_loss(y_pred: ArrayLike, y_true: ArrayLike) -> np.ndarray:
    """
    Compute cross entropy loss between true 1-hot encoded vector and softmax output of a predictor.
    """
    
    # Make sure to not have log(0)
    y_pred = np.clip(y_pred, eps, 1 - eps)
    # Compute cross entropy loss
    loss = -np.sum(np.log(y_pred)*y_true, axis = 1)

    # TODO : I think we need to sum twice in order to return a 1d output
    return np.log(np.mean(loss))