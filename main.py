from data import X, y
from train import train
from plots import plot_results

theta0 = 0
theta1 = 0
alpha = 0.01
iterations = 1000

theta0, theta1, cost_history = train(X, y, theta0, theta1, alpha, iterations)

plot_results(X, y, theta0, theta1, cost_history)