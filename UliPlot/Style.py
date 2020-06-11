#!/usr/bin/env python3
import matplotlib.pyplot as plt

__all__ = ["nice"]

def nice():
    """Set my preferred style: The ggplot style"""
    plt.style.use("ggplot")