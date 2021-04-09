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
from .unit   import UUnit
from .folder import UFolder
from .file   import UFile
from .netcdf import UNetcdf


class UFactory():
    """
        Creates a Units depending on the input value
    """

    @staticmethod
    def create(value, depth:int=0):
        """
            Creates the following units
                - Folder : value is string and it's a path to a folder
                - File   : value is string and it's a path to a file
        """
        if isinstance(value, str) and os.path.isdir(value):
            return UFolder(value, depth)
        if isinstance(value, str) and os.path.isfile(value):
            return UFile(value, depth)

        # Files Only
        if isinstance(value, UFile):
            if (value.label.endswith('.nc')):
                print("HERE" , value.path)
                return UNetcdf(value.path, depth)


    @staticmethod
    def create_from(unit:UUnit):
        """
            Creates Other Units from parents children
        """
        yield from (UFactory.create(x, unit.depth) for x in unit.children())
