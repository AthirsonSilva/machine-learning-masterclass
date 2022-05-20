# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

# large axes
axes1 = fig.add_axes([0, 0, 1, 1])

# small axes
axes2 = fig.add_axes([0, 0, 0.5, 0.5])

x = np.arange(0, 10)
y = x ** 4

axes1.plot(x, y)
axes2.plot(x / 2, y / 2)

fig

plt.show()
