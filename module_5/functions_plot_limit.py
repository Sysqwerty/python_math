import matplotlib.pyplot as plt
import numpy as np


# Побудуємо графік функції, для якого ми визначаємо границю. Для побудови графіка нам необхідно визначити інтервал, в якому на графіку буде змінюватися 𝑥
# Візьмемо змінну 𝑥 в інтервалі від -50 до 50 : x ∈ [−50;50]

# Data for plotting
x = np.arange(-50, 50, 0.01)
y = (7*(x**2)+7*x-2)/(x**2-2*x+3)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='x', ylabel='y',
       title='xy Graph')
ax.grid()

plt.show()
