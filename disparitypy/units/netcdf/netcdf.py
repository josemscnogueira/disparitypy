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
        return (UNetcdfGroup(self.path),)
