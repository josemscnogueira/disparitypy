# ##############################################################################
# System imports
# ##############################################################################
import itertools
from   netCDF4 import Dataset


# ##############################################################################
# Project imports
# ##############################################################################
from .unit      import UNetcdfAtomic
from .variable  import UNetcdfVariable
from .dimension import UNetcdfDimension
from .attribute import UNetcdfAttribute


class UNetcdfGroup(UNetcdfAtomic):
    """
        NetCDF group
    """
    # ##########################################################################
    # Interfaces from Abstract class UAtomic
    # ##########################################################################
    def _children_init(self):
        """
            PLACEHOLDER
        """
        self._children = tuple(self.__all_items)


    # ##########################################################################
    # NcGroup specific methods
    # ##########################################################################
    @property
    def __variables(self):
        for var in self().variables:
            yield UNetcdfVariable( self.path, name   = var        , \
                                              access = self.access, \
                                              parent = self.origin)
    @property
    def __dimensions(self):
        for dim in self().dimensions:
            yield UNetcdfDimension(self.path, name   = dim        , \
                                              access = self.access, \
                                              parent = self.origin)
    @property
    def __attributes(self):
        for att in self().ncattrs():
            yield UNetcdfAttribute(self.path, name   = att        , \
                                              access = self.access, \
                                              parent = self.origin)
    @property
    def __groups(self):
        for grp in self().groups:
            yield UNetcdfGroup(    self.path, name   = grp        , \
                                              access = self.access, \
                                              parent = self.origin)
    @property
    def __all_items(self):
        yield from itertools.chain(self.__variables ,
                                   self.__dimensions,
                                   self.__attributes,
                                   self.__groups    )
