import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)
n = 100

def update(curr):
    if curr == n: 
        a.event_source.stop()
    plt.cla()
    bins=np.arange(-7,21,0.5)
    plt.hist(x1[:curr], density=True, bins=bins, alpha=0.5)
    plt.hist(x2[:curr], density=True, bins=bins, alpha=0.5)
    plt.hist(x3[:curr], density=True, bins=bins, alpha=0.5)
    plt.hist(x4[:curr], density=True, bins=bins, alpha=0.5)
    plt.axis([-7,21,0,0.6])
    
a = animation.FuncAnimation(plt.figure(), update, interval=1)
plt.show()