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
from .unit             import UUnit
from .folder           import UFolder
from .file             import UFile
from .netcdf.netcdf    import UNetcdf
from .netcdf.group     import UNetcdfGroup
from .netcdf.variable  import UNetcdfVariable
from .netcdf.dimension import UNetcdfDimension
from .netcdf.attribute import UNetcdfAttribute


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
        # Folder instance
        if isinstance(value, str) and os.path.isdir(value):
            return UFolder(value)

        # File instance
        if isinstance(value, str) and os.path.isfile(value):
            return UFile(value)

        # File specializations
        if isinstance(value, UFile):
            if (value.label.endswith('.nc')):
                return UNetcdf(value.path)

        # Netcdf specializations
        if isinstance(value, UNetcdfGroup    ) or \
           isinstance(value, UNetcdfVariable ) or \
           isinstance(value, UNetcdfDimension) or \
           isinstance(value, UNetcdfAttribute):
            return value


    @staticmethod
    def create_from(unit:UUnit):
        """
            Creates Other Units from parents children
        """
        yield from (UFactory.create(x) for x in unit.children())
