"""
This file contains the data structures used in the program.
"""


class Derivative:
    """
    Base class for all derivatives
    """
    pass


class Option(Derivative):
    pass


class Strategy:
    """
    A strategy consists of any number of derivatives traded as a single block.
    """
    pass
