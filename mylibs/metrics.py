import numpy as np

def mse(y_true,y_pred):
    n = len(y_true)
    return np.sum((y_true - y_pred) ** 2) / n

def rmse(y_true,y_pred):
    return np.sqrt(mse(y_true,y_pred))

def mae(y_true,y_pred):
    n = len(y_true)
    return np.sum(abs(y_true - y_pred)) / n