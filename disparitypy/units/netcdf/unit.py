# ##############################################################################
# System imports
# ##############################################################################
import weakref
from   netCDF4 import Dataset

# ##############################################################################
# Project imports
# ##############################################################################
from ..unit import UCached


class UNetcdfAtomic(UCached):
    """
        Base (abstract) class for all netcdf items (variables, groups, dimensions)
    """
    # ##########################################################################
    # Attributes
    # ##########################################################################
    __origin:weakref    = None
    __ncid:Dataset      = None
    __path:str          = str()
    __access:tuple[str] = tuple()

    # ##########################################################################
    # Constructor
    # ##########################################################################
    def __init__(self, filepath:str, /, name   : str        = str(),   \
                                        access : tuple[str] = tuple(), \
                                        parent : weakref    = None):
        """
            Default constructor
        """
        # Call UAtomic Constructor
        self.__origin = parent or None
        self.__path   = filepath
        self.__access = (access + (name,)) if name else access
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
    def origin(self):
        """
            Returns origin:
                - it can be itself, if there is no origin
                - it can be origin provided in the constructor
        """
        return self.__origin or weakref.ref(self)


    @property
    def ncid(self):
        """
            Returns a valid handler to the underlying netcdf object
            Closing this asset is the responsability of the caller
        """
        if not self.__ncid:
            if self.__origin:
                self.__ncid = self.__origin().ncid
            else:
                self.__ncid = Dataset(self.path)

        return self.__ncid


    def close(self):
        """
            Removes and closes handle to underlyings netcdf object
            Let the garbage collector and the destructor of the netcdf Dataset
            object close the file access
        """
        self.__ncid = None


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
        result = self.ncid

        for elem in self.__access:
            result = result[elem]

        return result


    @property
    def path(self):
        """
            Returns the path of the underlying NetCDF file
        """
        return self.__path
