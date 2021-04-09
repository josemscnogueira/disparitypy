# ##############################################################################
# Project imports
# ##############################################################################
from .unit      import UNetcdfAtomic
from .attribute import UNetcdfAttribute


class UNetcdfVariable(UNetcdfAtomic):
    """
        NetCDF Variable
    """
    # ##########################################################################
    # Interfaces from Abstract class UAtomic
    # ##########################################################################
    def _children_init(self):
        """
            Variables have attributes
        """
        self._children = tuple(self.__attributes)

    @property
    def __attributes(self):
        for att in self().ncattrs():
            yield UNetcdfAttribute(self._context_manager, name=att, access=self.access)
