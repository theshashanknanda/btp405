import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
y = np.array([75, 60, 100, 125, 175, 200, 225, 210, 180, 140, 90, 80])

plt.plot(x, y)
plt.show()
