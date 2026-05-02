import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,10 ,100)

noise = 1.5 * np.random.randn(100)

y = 2.5* X + noise

plt.scatter(X, y)
plt.show()