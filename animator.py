
# https://matplotlib.org/examples/animation/dynamic_image.html
# https://stackoverflow.com/questions/17212722/matplotlib-imshow-how-to-animate
# http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
# https://stackoverflow.com/questions/17853680/animation-using-matplotlib-with-subplots-and-artistanimation
# https://stackoverflow.com/questions/9401658/how-to-animate-a-scatter-plot

import numpy as np
from matplotlib import animation
import cv2

def imgseq(fig, axs, fmts, range_frame, interval=50):
    ims = []
    for ax, fmt in zip(axs, fmts):
        img = cv2.imread(fmt.format(range_frame[0]), cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im = ax.imshow(img)
        ims.append(im)

    def read_frame(i_frame):
        for im, fmt in zip(ims, fmts):
            img = cv2.imread(fmt.format(range_frame[i_frame]), cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            im.set_data(img)
        return ims

    def init():
        return read_frame(0)

    def update(frame):
        return read_frame(frame)
    
    return animation.FuncAnimation(fig, update, frames=len(range_frame), interval=interval, init_func=init, blit=True)


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    # from IPython.display import HTML

    gridsize = (3, 2)
    fig = plt.figure(figsize=(12, 8))
    ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
    ax2 = plt.subplot2grid(gridsize, (2, 0))
    ax3 = plt.subplot2grid(gridsize, (2, 1))

    fmt = '../datasets/epfl_campus/CampusSeq1/Camera0/campus4-c0-{:05}.png'

    ani = imgseq(fig, [ax1,ax2,ax3], [fmt,fmt,fmt], range(100))
    plt.show()

   
#%%