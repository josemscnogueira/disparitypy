"""
    Creates units depending on a set of rules
"""

# ##############################################################################
# System Imports
# ##############################################################################
import os

# ##############################################################################
# Project Imports
# ##############################################################################
from .unit          import UUnit
from .folder        import UFolder
from .file          import UFile
from .netcdf.netcdf import UNetcdf


class UFactory():
    """
        Creates a Units depending on the input value
    """

    @staticmethod
    def create(value):
        """
            Creates the following units
                - Folder : value is string and it's a path to a folder
                - File   : value is string and it's a path to a file
        """
        if isinstance(value, str) and os.path.isdir(value):
            return UFolder(value)
        if isinstance(value, str) and os.path.isfile(value):
            return UFile(value)

        # Files Only
        if isinstance(value, UFile):
            if (value.label.endswith('.nc')):
                return UNetcdf(value.path)


    @staticmethod
    def create_from(unit:UUnit):
        """
            Creates Other Units from parents children
        """
        yield from (UFactory.create(x) for x in unit.children())
