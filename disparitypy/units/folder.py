"""
    Defines abstract class for Units supported for comparison
"""

# ##############################################################################
# System Imports
# ##############################################################################
import os

# ##############################################################################
# Project imports
# ##############################################################################
from .unit import UUnit


class UFolder(UUnit):
    """
        Folder for comparison
    """
    # ##########################################################################
    # Instance attributes
    # ##########################################################################
    _path : str


    # ##########################################################################
    # Methods
    # ##########################################################################
    def __init__(self, path:str):
        """
            Default Constructor
        """
        self._path = os.path.abspath(path)

    @property
    def path(self):
        return self._path


    # ##########################################################################
    # Methods from abstract class UUnit
    # ##########################################################################
    def children(self):
        """
            Returns other units contained inside this one
        """
        for item in os.listdir(self._path):
            yield os.path.join(self._path, item)

    def _label(self):
        """
            Representation of the instance
        """
        return os.path.basename(self._path)
