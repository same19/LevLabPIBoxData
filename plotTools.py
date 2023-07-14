from matplotlib import pyplot as plt
import numpy as np

def plotTwo(x,xlabel,f1,label1,f2,label2,color1="red",color2="blue"):
    fig, ax1 = plt.subplots()
    f1 = np.array(f1)
    f2 = np.array(f2)
    x = np.array(x)
    color = color1
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(label1, color=color)
    if f1.ndim > 1:
        for i in f1:
            ax1.plot(x,i,color=color)
    else:
        ax1.plot(x, f1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = color2
    ax2.set_ylabel(label2, color=color)  # we already handled the x-label with ax1
    if f2.ndim > 1:
        for i in f2:
            ax2.plot(x,i,color=color)
    else:
        ax2.plot(x, f2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    # fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

def polarPlot(theta,r, title):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r)
    ax.set_rmax(6)
    # ax.set_rticks([1,2,3,4,5,6,7,8,9,10,11,12])  # Less radial ticks
    # ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)

    ax.set_title(title, va='bottom')
    plt.show()