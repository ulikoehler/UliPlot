#!/usr/bin/env python3
from matplotlib import pyplot as plt

__all__ = ["figure"]

def figure(fig=None):
    """
    Return either fig or plt.gcf() if fig is None.
    """
    return plt.gcf() if fig is None else fig
