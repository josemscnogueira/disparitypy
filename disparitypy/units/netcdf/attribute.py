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
    def __eq__(self, other):
        """
            Two units are consired equal (in this case: comparable if)
        """
        if isinstance(other, type(self)):
            return self.__call__() == other()
        # Else
        return False


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
        assert self._context_manager.isopen()
        result = self._context_manager

        for elem in self.access[:-1]:
            result = result[elem]

        return getattr(result, self.access[-1])
