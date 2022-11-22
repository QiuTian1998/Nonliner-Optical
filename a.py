import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2*j + 1 for j in x]  
# 散点图
plt.scatter(x, y)
plt.show()

