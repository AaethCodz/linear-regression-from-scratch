import numpy as np
from model import hypothesis, compute_cost, gradient_descent

def train(X, y, theta0, theta1, alpha, iterations):
    cost_history = []
    
    for i in range(iterations):
        theta0, theta1 = gradient_descent(X, y, theta0, theta1, alpha)
        
        cost = compute_cost(X, y, theta0, theta1)
        cost_history.append(cost)
    
    return theta0, theta1, cost_history