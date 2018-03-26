import numpy as np

class SimpleLinearRegression:
    b0 = 0.0
    b1 = 0.0
    
    def __init__(self):
        """ Create a new point at the origin """
        self.b0 = 0.0
        self.b1 = 0.0
    
    def fit(self,X,y):
        X2 = []
        Y2 = []
        XY = []
        n = len(X)
        
        for i in range(0,n):
            X2.append(X[i] ** 2)
            Y2.append(y[i] ** 2)
            XY.append(X[i] * y[i])
            
        X2, Y2, XY = np.array(X2), np.array(Y2), np.array(XY)
        
        Sx2 = np.sum(X2) / n
        Sxy = np.sum(XY) / n
        Sy2 = np.sum(Y2) / n
        X_ = np.sum(X) / n
        y_ = np.sum(y) / n
        
        self.b1 = Sxy / Sx2
        self.b0 = y_ - (self.b1 * X_)
         
    def predict(self,X):
        y_pred = []
        for i in range(0,len(X)):
            y_pred.append(self.b0 + (self.b1 * X[i]))
        
        return np.array(y_pred)