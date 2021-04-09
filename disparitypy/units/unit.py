"""
    Defines abstract class for Units supported for comparison
"""

# ##############################################################################
# System Imports
# ##############################################################################
from abc import ABC, abstractmethod


class UUnit(ABC):
    """
        Abstract class for Units supported for comparison
    """
    __depth : int = 0


    # ##########################################################################
    # Abstract methods
    # ##########################################################################
    @abstractmethod
    def children(self):
        """
            Returns a list with other units
        """

    @abstractmethod
    def _label(self):
        """
            Returns a string representation of this unit
        """

    # ##########################################################################
    # Properties
    # ##########################################################################
    @property
    def label(self):
        return self._label()

    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, value : int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Depth value must be a non-negative integer value")
        self.__depth = value


    # ##########################################################################
    # Python built-in methods
    # ##########################################################################
    def __eq__(self, other):
        """
            Two units are consired equal (in this case: comparable if)
        """
        return isinstance(other, type(self)) and self.label == other.label

    def __hash__(self):
        """
            Hash function for this item depends on the class name and label
        """
        return hash((self.__class__.__name__, self._label()))

    def __repr__(self):
        """
            String repersentation of the object
        """
        #return f"{self.__class__.__name__}({self.label},{self.__hash__()})"
        return f"{self.__class__.__name__}({self.label})"
