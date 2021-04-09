# ##############################################################################
# System imports
# ##############################################################################
from   collections.abc import Iterable


# ##############################################################################
# Project imports
# ##############################################################################
from .unit import UNetcdfAtomic


class UNetcdfAttribute(UNetcdfAtomic):
    """
        NetCDF Attribute
    """
    # ##########################################################################
    # Interfaces from Abstract class UUnit
    # ##########################################################################
    def compare(self, other):
        """
            Two units are consired equal (in this case: comparable if)
        """
        result = False
        if isinstance(other, type(self)):
            result = self.__call__() == other()

            # There's instances where the result is a list/tuple/iterable
            if isinstance(result, Iterable):
                result = all(result)
        # Else
        return result


    # ##########################################################################
    # Interfaces from Abstract class UAtomic
    # ##########################################################################
    def _children_init(self):
        """
            Attributes have no children
        """


    # ##########################################################################
    # Override from UAtomic
    # ##########################################################################
    def __call__(self):
        """
            Accesses the underlying netcdf object
        """
        result = self.ncid

        for elem in self.access[:-1]:
            result = result[elem]

        return getattr(result, self.access[-1])
