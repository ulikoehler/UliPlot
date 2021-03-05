#!/usr/bin/env python3
from matplotlib import pyplot as plt
import matplotlib.ticker as mtick

def set_yaxis_tickformat_func(func, ax=None, set_major=True, set_minor=True):
    """
    For the current Y axis, set <func(value, index)> as the (major & minor) tick formatter.
    This is often used with lambda functions.
 
    Example usage:

    :param Function func: The formatter function (e.g. lambda value, index: ...)
    :param Axis ax: You can specify an ax object here. If None, plt.gca() is used.
    :param bool set_major: If True, set the formatter as major tick formatter
    :param bool set_minor: If True, set the formatter as minor tick formatter
    """
    if ax is None:
        ax = plt.gca()
    formatter = mtick.FuncFormatter(func)
    if set_major:
        ax.yaxis.set_major_formatter(formatter)
    if set_minor:
        ax.yaxis.set_minor_formatter(formatter)

def set_yaxis_tick_format(decimals=3, unit=None, ax=None, set_major=True, set_minor=True):
    """
    Set the number of decimals and the unit for formatting the Y axis.
    """
    # Create format string
    formatstr = f"%.{decimals}f"
    if unit is not None:
        formatstr += f" {unit}"
    # Create ax unless specfied
    if ax is None:
        ax = plt.gca()
    # Set formatter
    formatter = mtick.FormatStrFormatter(formatstr)
    if set_major:
        ax.yaxis.set_major_formatter(formatter)
    if set_minor:
        ax.yaxis.set_minor_formatter(formatter)
