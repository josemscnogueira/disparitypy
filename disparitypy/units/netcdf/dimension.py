# ##############################################################################
# Project imports
# ##############################################################################
from .unit import UNetcdfAtomic


class UNetcdfDimension(UNetcdfAtomic):
    """
        NetCDF Dimension
    """
    # ##########################################################################
    # Interfaces from Abstract class UAtomic
    # ##########################################################################
    def _children_init(self):
        """
            Dimensions have no children
        """
