import numpy as np

def standardize(X):
    X_ = []
    
    mean = np.mean(X)
    std = np.std(X)
    
    for i in X:
        X_.append((i - mean) / std)
        
    return np.array(X_)

def normalize(X):
    X_ = []
    
    min_ = np.min(X)
    max_ = np.max(X)
    
    for i in X:
        X_.append((i - min_) / (max_ - min_))
        
    return np.array(X_)