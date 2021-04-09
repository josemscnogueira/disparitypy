"""
    Defines abstract class for Units supported for comparison
"""

# ##############################################################################
# Project imports
# ##############################################################################
from .file import UFile


class UNetcdf(UFile):
    """
        Folder for comparison
    """
    def children(self):
        """
            Returns other units contained inside this one
        """
        return ()
