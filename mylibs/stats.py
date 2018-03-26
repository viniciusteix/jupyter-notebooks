import numpy as np

def mean(x):
    sum_ = np.sum(x)
    return sum_ / len(x)

def stdev(x):
    x_mean = mean(x)
    std_ = np.sum((x - x_mean) ** 2)
    return np.sqrt(std_ / len(x))

def var(x):
    x_mean = mean(x)
    var_ = np.sum((x - x_mean) ** 2)
    return var_ / len(x)