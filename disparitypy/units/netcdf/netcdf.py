"""
    Defines abstract class for Units supported for comparison
"""
# ##############################################################################
# System imports
# ##############################################################################
from netCDF4 import Dataset

# ##############################################################################
# Project imports
# ##############################################################################
from ..file import UFile
from .group import UNetcdfGroup


class UNetcdf(UFile):
    """
        Folder for comparison
    """
    def children(self):
        """
            Returns other units contained inside this one
        """
        with Dataset(self.path) as ncid:
            result = (UNetcdfGroup(ncid),)

            print(list(result[0].children()))

            exit(0)

            return result
