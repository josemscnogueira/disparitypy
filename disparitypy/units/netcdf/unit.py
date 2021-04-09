# ##############################################################################
# System imports
# ##############################################################################
from netCDF4 import Dataset

# ##############################################################################
# Project imports
# ##############################################################################
from ..unit import UAtomic


class UNetcdfAtomic(UAtomic):
    """
        Base (abstract) class for all netcdf items (variables, groups, dimensions)
    """
    # ##########################################################################
    # Attributes
    # ##########################################################################
    __access:tuple[str] = tuple()

    # ##########################################################################
    # Constructor
    # ##########################################################################
    def __init__(self, context_manager:Dataset, /, name:str=str(), access:tuple[str]=tuple()):
        """
            Default constructor
        """
        # Call UAtomic Constructor
        self._context_manager = context_manager
        self.__access         = (access + (name,)) if name else access
        super().__init__()



    # ##########################################################################
    # Interfaces from Abstract class UUnit
    # ##########################################################################
    def _label(self):
        """
            Label is a concatenation of the original access and name
        """
        return self.__access[-1] if self.__access else str()


    # ##########################################################################
    # Utility methods
    # ##########################################################################
    @property
    def access(self):
        """
            Retrives access tuple
        """
        return self.__access


    def __call__(self):
        """
            Accesses the underlying netcdf object
        """
        assert self._context_manager.isopen()
        result = self._context_manager

        for elem in self.__access:
            result = result[elem]

        return result


    @property
    def path(self):
        return self._context_manager.filepath()
