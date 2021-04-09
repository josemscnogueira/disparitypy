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
from .folder import UFolder


class UFile(UFolder):
    """
        Folder for comparison
    """
    def children(self):
        """
            Returns other units contained inside this one
        """
        return ()
