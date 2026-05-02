import numpy as np

def hypothesis(X, theta0, theta1):
    return theta0 + X *theta1

def compute_cost(X, y, theta0, theta1):
    y_pred = hypothesis(X, theta0, theta1)
    
    error = y_pred - y
    
    cost = (1 / len(y)) * np.sum(error ** 2)
    
    return cost

def gradient_descent(X, y, theta0, theta1, alpha):
    y_pred =hypothesis(X, theta0, theta1)
    
    error = y_pred - y
    
    d_theta0 = (2 / len(y)) * np.sum(error)
    
    d_theta1 = (2 / len(y)) * np.sum(error * X)
    
    theta0 = theta0 - alpha * d_theta0
    theta1 = theta1 - alpha * d_theta1
    
    return theta0, theta1