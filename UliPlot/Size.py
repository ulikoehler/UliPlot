#!/usr/bin/env python3
from .Figure import figure

__all__ = ["huge", "size"]

def size(w=15, h=8, fig=None):
    """
    Set the figure to the given size in inches
    """
    figure(fig).set_size_inches(w, h)

def huge(fig=None):
    """
    Make the figure huge: 20x10 inches
    """
    size(20, 10, fig)

def normal(fig=None):
    """
    Make the figure large: 15x8 inches
    """
    size(15, 8, fig)

def wide(fig=None):
    """
    Make the figure large & wide: 15x5 inches
    """
    size(15, 5, fig)

def huge_wide(fig=None):
    """
    Make the figure large & wide: 20x7 inches
    """
    size(20, 7, fig)
