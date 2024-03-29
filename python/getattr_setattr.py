from typing import List, Any, Type, Optional


class Thing:
    """

    """
    def __init__(self):
        # need to use __dict__ here because otherwise __setattr__ gets invoked
        # set to true to prevent members of this config object from being changed
        self.__dict__['locked'] = False

    # override setattr behavior so that we can directly access config variable
    # values, and prevent overriding values when locked
    def __setattr__(self, name: str, value: Any):
        if self.locked and not name == '_locked':
            raise Exception("object is locked")
        object.__setattr__(self, name, value)
        # also have to add to dict, because it's not handled by above line
        self.__dict__[name] = value

    # override getattr behavior to directly return value of config variables
    def __getattribute__(self, name: str) -> Any:
        val = object.__getattribute__(self, name)
        return val

    # annoyingly, we have to implement these two methods for the Thing object to be picklable
    # they will be found by the val = object.__getattribute__(self, name) in __getattribute__ above
    def __getstate__(self):
        return self.__dict__
    def __setstate__(self, state):
        # have to add this to the dict before setting to a new thing, because of 
        # the mechanics of __setattr__ above. Shrug.
        self.__dict__['locked'] = False
        self.__dict__ = state

    def get_item(self, name: str):
        return self.__dict__[name]
