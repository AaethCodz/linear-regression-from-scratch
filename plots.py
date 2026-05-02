import matplotlib.pyplot as plt
from model import hypothesis

def plot_results(X, y, theta0, theta1, cost_history):
    
    # plot data + best fit line
    plt.scatter(X, y)
    
    y_pred = hypothesis(X, theta0, theta1)
    plt.plot(X, y_pred, color='red')
    
    plt.title("Best Fit Line")
    plt.show()
    
    #plot cost vs iterations
    plt.plot(cost_history)
    plt.title("Loss vs Iterations")
    plt.show()