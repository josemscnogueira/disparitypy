# ##############################################################################
# System Imports
# ##############################################################################
from enum import Enum


# ##############################################################################
# Project Imports
# ##############################################################################
from ..units.unit         import UUnit
from ..units.factory      import UFactory

class ComparisonStatus(Enum):
    UNINITIALIZED = 0
    PENDING       = 1
    EQUAL         = 2
    DIFFERENT     = 3


class ComparisonResult():
    """
        Class for results
    """
    __status  : ComparisonStatus = ComparisonStatus.UNINITIALIZED
    __message : str
    __units   : tuple


    def __init__(self, unit1:UUnit, unit2:UUnit):
        """
            Default Constructor
        """
        self.__status  = ComparisonStatus.PENDING
        self.__units   = (unit1, unit2)


    def resolve(self):
        """
            Resolves by comparing unit 1 to unit 2
        """
        # Check for absent unit
        # Sometimes product #1 may have a unit while product #2 doesn't and
        # vice-versa
        if any((x is None for x in self.__units)):
            self.__status = ComparisonStatus.DIFFERENT
            return

        # Else, process children
        child_1_only, child_2_only, child_common = self._align_children()

        for child in child_1_only:
            yield ComparisonResult(child, None)

        for child in child_2_only:
            yield ComparisonResult(None,  child)

        for child1, child2 in child_common:
            yield ComparisonResult(child1,  child2)


    def __repr__(self):
        """
            String representation
        """
        return f"{self.__units[0]} Vs. {self.__units[1]} : {self.__status}"

    # ##########################################################################
    # Private methods
    # ##########################################################################
    def _align_children(self):
        """
            Returns a tuple containing
            - children units only in unit #1
            - children units only in unit #2
            - children units common to both units for comparison
        """
        child_1      = set(map(lambda x : UFactory.create(x, self.__units[0].depth + 1), self.__units[0].children()))
        child_2      = set(map(lambda x : UFactory.create(x, self.__units[1].depth + 1), self.__units[1].children()))
        child_common = child_1 & child_2
        child_1_only = child_1 - child_common
        child_2_only = child_2 - child_common

        return child_1_only, \
               child_2_only, \
               zip(child_common | child_1, child_common | child_2)
