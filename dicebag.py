"""
dicebag - an infinite bag of dice.
"""

import random
import re
import sys


def _roll_func(count, sides):
    """
    Return a function which will roll a die with a number of `sides`, `count` times, and return the total.
    """

    def _roll():
        return sum(random.randint(1, sides) for _ in range(count))

    _roll.__name__ = f"roll_{count}d{sides}"

    return _roll


class DiceBag:
    """
    An infinite bag of dice.
    
    >>> import dicebag
    >>> dicebag.roll_d6()
    5
    >>> dicebag.roll_3d6()
    9
    >>> dicebag.roll_2d50()
    43
    """

    def __getattr__(self, name):
        match = re.match(r"roll_(?P<count>\d*)d(?P<sides>\d+)", name)
        if match:
            count_string = match.group("count")
            if count_string == "":
                count = 1
            else:
                count = int(count_string)
            sides = int(match.group("sides"))
            return _roll_func(count, sides)
        raise AttributeError(f"{__class__.__name__!r} object has no attribute {name!r}")


# Replace this module with an instance of DiceBag:
sys.modules[__name__] = DiceBag()
