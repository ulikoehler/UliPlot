#!/usr/bin/env python3
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

def set_num_xticks(nticks, ax=None):
    """
    For the X axis, set a constant number of ticks, computing the
    tick spacing in <nticks> equidistant steps from start to stop.
    """
    if ax is None:
        ax = plt.gca()
    ax.xaxis.set_major_locator(mtick.LinearLocator(nticks))

def set_num_yticks(nticks, ax=None):
    """
    For the Y axis, set a constant number of ticks, computing the
    tick spacing in <nticks> equidistant steps from start to stop.
    """
    if ax is None:
        ax = plt.gca()
    ax.yaxis.set_major_locator(mtick.LinearLocator(nticks))
