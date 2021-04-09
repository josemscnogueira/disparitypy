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
    def is_leaf(self):
        """
            Returns true at firt child occurrence
            Returns false if no children (default of any)
        """
        return any(True for _ in self.children())

    @property
    def label(self):
        return self._label()

    def close(self):
        """
            Do nothing, there's no assets associated with this abstract class
            This method is useful is a specific unit is associated with a resource
            that shoulbe be closed after using it completly.
            e.g. when the comparator/result analyse two units, often the unit
                 also has children which use the same resources. the comparator
                 works by analysing everything in depth, which guarantees that a
                 specific unit has its comparison done when all of its children
                 are analyized. it might be useful to call close() at that time
        """

    def compare(self, other):
        """
            This is the method that will be used to compare two units of the same
            type with the same label
            By default, this comparison will be exactly like __eq__ (== operator)
        """
        return self == other

    # ##########################################################################
    # Python built-in methods
    # ##########################################################################
    def __eq__(self, other):
        """
            Two units are consired equal (in this case: comparable if)
        """
        return self.__class__ == other.__class__ and self.label == other.label

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



class UCached(UUnit):
    """
        Abstract class exactly as UUnit, but children are created on constructor,
        and access is limited to a context manager

        Instances should be considered immutable
    """
    _children:tuple[UUnit] = tuple()


    def __init__(self):
        """
            Default constructor should populate children
            Context manager can't be none
        """
        self._children_init()


    def children(self):
        yield from self._children


    # ##########################################################################
    # Abstract methods to implement
    # ##########################################################################
    @abstractmethod
    def _children_init(self):
        """
            Populates _children
            In principle, these children should be created using the context
            manager.
        """
