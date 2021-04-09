"""
    Defines abstract class for Units supported for comparison
"""
# ##############################################################################
# Project imports
# ##############################################################################
from .folder import UFolder


class UFile(UFolder):
    """
        File for comparison
    """
    def children(self):
        """
            Returns other units contained inside this one
        """
        return (self,)


class UFileGeneric(UFile):
    """
        Generic File Unit
    """
    def children(self):
        return tuple()
