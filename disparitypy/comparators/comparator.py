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
    __queue  : Queue = Queue()


    def __init__(self, unit1 : UUnit, unit2 : UUnit):
        """
            Default Constructor
        """
        self.__result = ComparisonResult(unit1, unit2)
        self.__queue.put(self.__result)


    def compare(self):
        """
            Returns a comparison result Unit
        """
        # Process all comparisons in queue
        while not self.__queue.empty():
            # Get the last item inserted
            item = self.__queue.get()

            # Solve sub-sequent (nested) comparisons
            for child in item.resolve():
                if child is not None:
                    self.__queue.put(child)

            print(item)

        return self.__result


    @staticmethod
    def from_paths(path1 : str, path2 : str):
        """
            Creates 'root' Comparator from paths
            (which can be provided via command line or GUI)
        """
        return UComparator(UFactory.create(path1),
                           UFactory.create(path2))
