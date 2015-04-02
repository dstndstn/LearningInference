# numpy: numerical library
import numpy as np
# avoid broken installs by forcing Agg backend...
#import matplotlib
#matplotlib.use('Agg')
# pylab: matplotlib's matlab-like interface
import pylab as plt

# The data we will fit:
#  x, y, sigma_y
data1 = np.array([[201,592,61],[244,401,25],[47,583,38],[287,402,15],[203,495,21],
                  [58,173,15],[210,479,27],[202,504,14],[198,510,30],[158,416,16],
                  [165,393,14],[201,442,25],[157,317,52],[131,311,16],[166,400,34],
                  [160,337,31],[186,423,42],[125,334,26],[218,533,16],[146,344,22]])

# plotting limits
xlimits = [0,250]
ylimits = [100,600]
title_prefix = 'Straight line'
plot_format = '.png'

mlimits = [1.5, 3.5]
blimits = [0, 60]

def get_data_no_outliers():
    # pull out the x, y, and sigma_y columns, which have been packed into the
    # "data1" matrix.  "data1" has shape (20,3).  ":" means "everything in
    # that dimension".  Some of the first 5 points are outliers so for this
    # part we only grab from index 5 on, with magic "5:"
    x = data1[5:,0]
    y = data1[5:,1]
    sigmay = data1[5:,2]
    return (x, y, sigmay)

# Plot data with error bars, standard axis limits, etc.
def plot_yerr(x, y, sigmay):
    # plot data with error bars
    plt.errorbar(x, y, yerr=sigmay, fmt='.', ms=7, lw=1, color='k')
    # if you put '$' in you can make Latex labels
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.xlim(*xlimits)
    plt.ylim(*ylimits)
    plt.title(title_prefix)

# Plot a   y = mx + b  line.
def plot_line(m, b, **kwargs):
    x = np.array(xlimits)
    y = b + m*x
    p = plt.plot(x, y, 'k-', alpha=0.5, **kwargs)
    plt.xlim(*xlimits)
    plt.ylim(*ylimits)
    return p



