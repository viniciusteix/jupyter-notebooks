import numpy as np

def split_train_test(n_elem, perc_train, seed):
    a = [ i for i in range(n_elem) ]
    np.random.seed(seed)
    np.random.shuffle(a)
    
    n_train = int(round(n_elem * perc_train))
    
    train_ = a[:n_train]
    test_ = a[n_train:]
    
    r = (train_,test_)
    
    return r