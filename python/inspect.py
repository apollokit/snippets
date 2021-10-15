import sys
import inspect

class SuperClass:
    pass
class SubClass1:
    pass
class SubClass2:
    pass

_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
_local_packet_classes = [c[1] for c in _classes if (issubclass(c[1], SuperClass) and not c[1] is SuperClass)]
# contains [SubClass1, SubClass2]