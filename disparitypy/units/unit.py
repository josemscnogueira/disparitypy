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



class UAtomic(UUnit):
    """
        Abstract class exactly as UUnit, but children are created on constructor,
        and access is limited to a context manager

        Instances should be considered immutable
    """
    _children        : tuple[UUnit]
    _context_manager : object = None


    def __init__(self):
        """
            Default constructor should populate children
            Context manager can't be none
        """
        assert self._context_manager is not None
        self._children_init()

    @abstractmethod
    def _children_init(self):
        """
            Populates _children
            In principle, these children should be created using the context
            manager.
        """

    def children(self):
        yield from self._children
