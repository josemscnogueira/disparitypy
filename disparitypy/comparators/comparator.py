# ##############################################################################
# System Imports
# ##############################################################################
from queue import Queue

# ##############################################################################
# Project Imports
# ##############################################################################
from ..units.unit         import UUnit
from ..units.factory      import UFactory

from .result              import ComparisonResult


class UComparator():
    """
        Class that compares two units
    """
    # Instance attributes
    __result : ComparisonResult


    def __init__(self, unit1 : UUnit, unit2 : UUnit):
        """
            Default Constructor
        """
        self.__result = ComparisonResult(unit1, unit2)


    def compare(self):
        """
            Returns a comparison result Unit
        """
        queue = Queue()
        queue.put(self.__result)

        # Process all comparisons in queue
        while not queue.empty():
            # Get the last item inserted
            item:ComparisonResult = queue.get()

            # Solve sub-sequent (nested) comparisons
            for child in item.resolve():
                # FIXME: remove if and assert
                assert child is not None
                if child is not None:
                    queue.put(child)

            # FIXME: remove please
            # FIXME: remove please
            # FIXME: remove please
            if item.is_leaf():
                print(item)
            # FIXME: remove please
            # FIXME: remove please
            # FIXME: remove please

        return self.__result


    @staticmethod
    def from_paths(path1 : str, path2 : str):
        """
            Creates 'root' Comparator from paths
            (which can be provided via command line or GUI)
        """
        return UComparator(UFactory.create(path1),
                           UFactory.create(path2))
