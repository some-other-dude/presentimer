"""
clock.py holds the Clock class
"""


import time
import multiprocessing
import tkinter


class Clock:
    """
    Clock objects

    Clock objects are the individual timers.  This class instantiates a clock and manages the data interchange
    of the clockself.

    Time is always in seconds.

    Colors are from tkinter.

    Parameters
    ----------
    total_time : int
        Total time the clock is to count from.
    remaining_time : int
        Time reimaining until zero.  Negative values indicate an over time state.
    is_running : bool
        Current running state of the clock.
    activebackground : color constant
        Background color for the widget when the widget is active.
    activeforeground : color constant
        Foreground color for the widget when the widget is active.
    background : color constant
        Background color for the widget.
    foreground : color constant
        Foreground color for the widget.

    Returns
    ----------
    none

    """

    def __init__(self,
                name = "New Clock",
                total_time = 0,
                remaining_time = 0,
                is_running = False,
                activebackground = 'firebrick',
                activeforeground = 'red',
                background = 'black',
                foreground = 'red',
                clock_process_id = None
                ):

        self.name = name
        self.total_time = total_time
        self.remaining_time = remaining_time
        self.is_running = is_running
        self.activebackground = activebackground
        self.activeforeground = activeforeground
        self.background = background
        self.foreground = foreground
        self.clock_process_id = clock_process_id


    #GETTERS
    def get_name(self):
        return self.name

    def get_total_time(self):
        return self.current_time

    def get_remaing_time(self):
        return self.remaining_time

    def get_is_running(self):
        return self.is_running

    def get_activebackground(self):
        return self.activebackground

    def get_activeforeground(self):
        return self.activeforeground

    def get_background(self):
        return self.background

    def get_foreground(self):
        return self.foreground

    def get_clock_process_id(self):
        return self.clock_process_id

    #SETTERS

    def set_name(self, new_value):
        self.name = new_value

    def set_total_time(self, new_value):
        self.current_time = new_value

    def set_remaing_time(self, new_value):
        self.remaining_time = new_value

    def set_is_running(self, new_value):
        self.is_running = new_value

    def set_activebackground(self, new_value):
        self.activebackground = new_value

    def set_activeforeground(self, new_value):
        self.activeforeground = new_value

    def set_background(self, new_value):
        self.background = new_value

    def set_foreground(self, new_value):
        self.foreground = new_value

    def set_clock_process_id(self):
        return self.clock_process_id
