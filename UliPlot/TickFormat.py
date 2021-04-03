#!/usr/bin/env python3
from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdates

def set_axis_tick_format_func(func, axis, set_major=True, set_minor=True):
    """
    Set the tick formatter for an X or Y axis to set_axis_tick_format_func
    Typically, this is not called directly.
    Usually you should use set_xaxis_tick_format_func() or set_yaxis_tick_format_func()
    instead.
    """
    formatter = mtick.FuncFormatter(func)
    if set_major:
        axis.set_major_formatter(formatter)
    if set_minor:
        axis.set_minor_formatter(formatter)

def set_yaxis_tick_format_func(func, ax=None, set_major=True, set_minor=True):
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
    set_axis_tick_format_func(func, ax.yaxis, set_major=set_major, set_minor=set_minor)


def set_xaxis_tick_format_func(func, ax=None, set_major=True, set_minor=True):
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
    set_axis_tick_format_func(func, ax.xaxis, set_major=set_major, set_minor=set_minor)

def set_axis_tick_format_float(axis, decimals=3, unit=None, set_major=True, set_minor=True):
    """
    Set the number of decimals and the unit for formatting the given X or Y axis.
    Typically, this is not called directly.
    Usually you should use set_xaxis_tick_format_float() or set_yaxis_tick_format_float()
    instead.
    """
    # Create format string
    formatstr = f"%.{decimals}f"
    if unit is not None:
        formatstr += f" {unit}"
    # Set formatter
    formatter = mtick.FormatStrFormatter(formatstr)
    if set_major:
        axis.set_major_formatter(formatter)
    if set_minor:
        axis.set_minor_formatter(formatter)

def set_yaxis_tick_format_float(decimals=3, unit=None, ax=None, set_major=True, set_minor=True):
    """
    Set the number of decimals and the unit for formatting the Y axis.
    """
    # Create ax unless specfied
    if ax is None:
        ax = plt.gca()
    # Set formatter
    set_axis_tick_format_float(ax.yaxis, decimals=decimals, unit=unit, set_major=set_major, set_minor=set_minor)

def set_xaxis_tick_format_float(decimals=3, unit=None, ax=None, set_major=True, set_minor=True):
    """
    Set the number of decimals and the unit for formatting the Y axis.
    """
    # Create ax unless specfied
    if ax is None:
        ax = plt.gca()
    # Set formatter
    set_axis_tick_format_float(ax.xaxis, decimals=decimals, unit=unit, set_major=set_major, set_minor=set_minor)

def set_axis_tick_format_datetime(axis, dateformat="%Y%m%d %H%M%S", tz=None, set_major=True, set_minor=True):
    """
    Set the date format for formatting the given X or Y axis.
    Typically, this is not called directly.
    Usually you should use set_xaxis_tick_format_datetime() or set_yaxis_tick_format_datetime()
    instead.

    :param axis: The axis (X or Y) to set the formatter for
    :param str dateformat: The strftime date format string, e.g. "%Y%m%d %H%M%S"
    :param datetime.tzinfo tz: The time zone for the ticks, uses matplotlib default if None
    :param bool set_major: If True, set the formatter as major tick formatter
    :param bool set_minor: If True, set the formatter as minor tick formatter
    """
    # Set formatter
    formatter = mdates.DateFormatter(dateformat, tz=tz)
    if set_major:
        axis.set_major_formatter(formatter)
    if set_minor:
        axis.set_minor_formatter(formatter)


def set_yaxis_tick_format_datetime(dateformat="%Y-%m-%d %H:%M:%S", tz=None, ax=None, set_major=True, set_minor=True):
    """
    Configure the Y axis with datetime format ticks
    
    :param str dateformat: The strftime date format string, e.g. "%Y%m%d %H%M%S"
    :param datetime.tzinfo tz: The time zone for the ticks, uses matplotlib default if None
    :param Axis ax: You can specify an ax object here. If None, plt.gca() is used.
    :param bool set_major: If True, set the formatter as major tick formatter
    :param bool set_minor: If True, set the formatter as minor tick formatter
    """
    # Create ax unless specfied
    if ax is None:
        ax = plt.gca()
    # Set formatter
    set_axis_tick_format_datetime(ax.yaxis, dateformat=dateformat, tz=tz, set_major=set_major, set_minor=set_minor)

def set_xaxis_tick_format_datetime(dateformat="%Y-%m-%d %H:%M:%S", tz=None, ax=None, set_major=True, set_minor=True):
    """
    Configure the X axis with datetime format ticks
    
    :param str dateformat: The strftime date format string, e.g. "%Y%m%d %H%M%S"
    :param datetime.tzinfo tz: The time zone for the ticks, uses matplotlib default if None
    :param Axis ax: You can specify an ax object here. If None, plt.gca() is used.
    :param bool set_major: If True, set the formatter as major tick formatter
    :param bool set_minor: If True, set the formatter as minor tick formatter
    """
    # Create ax unless specfied
    if ax is None:
        ax = plt.gca()
    # Set formatter
    set_axis_tick_format_datetime(ax.xaxis, dateformat=dateformat, tz=tz, set_major=set_major, set_minor=set_minor)

def set_axis_tick_format_percent(axis, fullscale=1.0, set_major=True, set_minor=True):
    """
    Set the percent format for formatting the given X or Y axis.
    Typically, this is not called directly.
    Usually you should use set_xaxis_tick_format_percent() or set_yaxis_tick_format_percent()
    instead.

    :param axis: The axis (X or Y) to set the formatter for
    :param fullscale: What value is considered to be 100%. Use 100.0 for values that are already scaled as percent.
    :param bool set_major: If True, set the formatter as major tick formatter
    :param bool set_minor: If True, set the formatter as minor tick formatter
    """
    # Set formatter
    formatter = mtick.PercentFormatter(fullscale)
    if set_major:
        axis.set_major_formatter(formatter)
    if set_minor:
        axis.set_minor_formatter(formatter)


def set_yaxis_tick_format_percent(fullscale=1.0, ax=None, set_major=True, set_minor=True):
    """
    Set the number of decimals and the unit for formatting the Y axis.
    
    :param fullscale: What value is considered to be 100%. Use 100.0 for values that are already scaled as percent.
    :param Axis ax: You can specify an ax object here. If None, plt.gca() is used.
    :param bool set_major: If True, set the formatter as major tick formatter
    :param bool set_minor: If True, set the formatter as minor tick formatter
    """
    # Create ax unless specfied
    if ax is None:
        ax = plt.gca()
    # Set formatter
    set_axis_tick_format_percent(ax.yaxis, fullscale, set_major=set_major, set_minor=set_minor)

def set_xaxis_tick_format_percent(fullscale=1.0, ax=None, set_major=True, set_minor=True):
    """
    Set the number of decimals and the unit for formatting the X axis.
    
    :param fullscale: What value is considered to be 100%. Use 100.0 for values that are already scaled as percent.
    :param Axis ax: You can specify an ax object here. If None, plt.gca() is used.
    :param bool set_major: If True, set the formatter as major tick formatter
    :param bool set_minor: If True, set the formatter as minor tick formatter
    """
    # Create ax unless specfied
    if ax is None:
        ax = plt.gca()
    # Set formatter
    set_axis_tick_format_datetime(ax.xaxis, fullscale, set_major=set_major, set_minor=set_minor)
