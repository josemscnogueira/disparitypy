# ##############################################################################
# System Imports
# ##############################################################################
import weakref
from   enum    import Enum


# ##############################################################################
# Project Imports
# ##############################################################################
from ..units.unit         import UUnit
from ..units.factory      import UFactory

class ComparisonStatus(Enum):
    UNINITIALIZED = 0
    DIFFERENT     = 1
    PENDING       = 2
    EQUAL         = 3

    def __lt__(self, other):
        return isinstance(other, type(self)) and self.value == other.value

    @staticmethod
    def create(value1, value2):
        return ComparisonStatus.EQUAL if value1 == value2 \
          else ComparisonStatus.DIFFERENT




class ComparisonResult():
    """
        Class for results
    """
    __status   : ComparisonStatus = ComparisonStatus.UNINITIALIZED
    __message  : str
    __units    : tuple
    __parent   : weakref
    __children : list = list()


    def __init__(self, unit1:UUnit, unit2:UUnit, parent = None):
        """
            Default Constructor
        """
        self.__status  = ComparisonStatus.PENDING
        self.__units   = (unit1, unit2, ComparisonStatus.create(unit1, unit2))
        self.__parent  = weakref.ref(parent) if parent is not None else None


    def resolve(self):
        """
            Resolves by comparing unit 1 to unit 2
        """
        # Process children
        # Children will be empty if any unit is None
        child_1_only, child_2_only, child_common = self._align_children()
        self.__children = list()
        self.__children.extend(ComparisonResult(x1  , None, self) for x1    in child_1_only)
        self.__children.extend(ComparisonResult(None, x2  , self) for x2    in child_2_only)
        self.__children.extend(ComparisonResult(x1  , x2  , self) for x1,x2 in child_common if x1 is not None and x2 is not None)

        yield from self.__children

        # Compare itself
        self.update()


    @property
    def status(self):
        """
            Getter for status
        """
        return self.__status

    @status.setter
    def status(self, value : ComparisonStatus):
        """
            Updates status and notifies parent in case status was changed
        """
        if (value != self.__status):
            self.__status = value

            if (self.__parent):
                self.__parent().notify()

        return self.__status


    def update(self):
        """
            Updates self status if current status is pending
              - and children are no longer pending
              - (or) has no children
        """
        if self.status == ComparisonStatus.PENDING and \
            all(map(lambda x: x.status != ComparisonStatus.PENDING, self.__children)):
            self.notify()

    def notify(self):
        """
            Updates status according to children status and its own
            This function is called when a status is changed and it propagates
            to parents (via status.setter)
        """
        self.status = min(self.__units[-1], min((x.status for x in self.__children), default=ComparisonStatus.EQUAL))


    def is_leaf(self):
        """
            A result is a leaf if there's no children,
            Status must also be final (equal or different)
        """
        if (self.status == ComparisonStatus.DIFFERENT or \
            self.status == ComparisonStatus.EQUAL   ) and len(self.__children) == 0:
            return True

        # Else
        return False


    def __repr__(self):
        """
            String representation
        """
        return f"{self.__units[0]} Vs. {self.__units[1]} : {self.status}"

    # ##########################################################################
    # Private methods
    # ##########################################################################
    def _align_children(self):
        """
            Returns a tuple containing
            - children units only in unit #1
            - children units only in unit #2
            - children units common to both units for comparison

            Tuples will be be empty if unit1 or unit is None
        """
        if any((x is None for x in self.__units)):
            return tuple(), tuple(), tuple()

        child_1      = tuple(UFactory.create(x) for x in self.__units[0].children())
        child_2      = tuple(UFactory.create(x) for x in self.__units[1].children())
        child_1_only = tuple(x for x in child_1 if x not in child_2)
        child_2_only = tuple(x for x in child_2 if x not in child_1)
        child_common = tuple(zip((x for x in child_1 if x not in child_1_only), \
                                 (x for x in child_2 if x not in child_2_only)))

        return child_1_only, \
               child_2_only, \
               child_common
