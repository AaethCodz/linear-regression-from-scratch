# Linear Regression from Scratch

This project was developed for my own understanding of linear regression, rather than relying on ready-made libraries.

The model learns the dependency between X and y by minimizing the cost function with gradient descent. All calculations are done purely in NumPy, while all visualizations are done in Matplotlib.

## How to run

1. Install dependencies:
pip install -r requirements.txt

2. Run the script:
python main.py

## What it does

1. Creates a synthetic dataset with some noise
2. Develops a linear regression model from scratch
3. Visualizes:
  - Best fit line
  - Loss per iteration

## Details

1. The model starts with some random weights and biases, which gradually become more optimal
2. One can observe the decrease in the loss function as training proceeds
3. Quickly converges (after about a hundred iterations)

## Why I built this

I created this project to better understand how machine learning models optimize their parameters.