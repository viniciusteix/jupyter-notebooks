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

def split_k_fold(n_elem, n_splits = 3, shuffle = True, seed = 0):
    a = [ i for i in range(n_elem) ]
    np.random.seed(seed)
    if shuffle:
        np.random.shuffle(a)
    
    n_test = int(round(n_elem * (1.0 / n_splits)))
    n_train = n_elem - n_test
    
    train = []
    test = []
#     print(a)
#     print(n_test)
    
    for i in range(n_splits):
#         print(i)
        flag = False
        flag_ = False
        
        if(i == n_splits-1):
            flag_ = True
        
        train_ = []
        test_ = []
        
        if(flag_):
            for j in range(n_elem):
                if(j <= i*n_test):
                    train_.append(a[j])
                else:
                    test_.append(a[j])
                
        else:
            for j in range(n_elem):
                if( j >= (i*n_test) and j < ( (i+1)*n_test )):
                    flag = True
                else:
                    flag = False

                if(flag):
                    test_.append(a[j])
                else:
                    train_.append(a[j])
            
        train.append(train_)
        test.append(test_)
            
    return np.array(train),np.array(test)
            
            
            
            
            
            
            
            
            
            
            
            
            
            