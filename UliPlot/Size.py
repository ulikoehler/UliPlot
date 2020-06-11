#!/usr/bin/env python3
from .Figure import figure

__all__ = ["huge", "size", "medium", "medium_square", "large", "wide", "huge_wide"]

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

def medium(fig=None):
    """
    Make the figure medium: 10x5 inches
    """
    size(10, 5, fig)

def medium_square(fig=None):
    """
    Make the figure a medium square: 7x7 inches
    """
    size(7, 7, fig)

def large(fig=None):
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
