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
    # Instance attributes
    _path : str


    def __init__(self, path:str, depth:int):
        """
            Default Constructor
        """
        self._path = os.path.abspath(path)
        self.depth = depth

    def children(self):
        """
            Returns other units contained inside this one
        """
        for item in os.listdir(self._path):
            yield os.path.join(self._path, item)

    def label(self):
        """
            Representation of the instance
        """
        return os.path.basename(self._path)
