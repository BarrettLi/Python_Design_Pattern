# -*- coding: utf-8 -*-

class Singleton(object):

    # Singleton

    class _A(object):
        # invisible to the outside
        def __init__(self):
            pass

        def display(self):
            # return the ID of current instance, it is globally distinct
            return id(self)

    # instance variable used to store the instance of _A
    _instance = None

    def __init__(self):
        # if there is no instance of _A, then create one
        if Singleton._instance is None:
            Singleton._instance = Singleton._A()
    
    def __getattr__(self,attr):
        # all of the attributes should be obtained from Singleton._instance
        return getattr(self._instance, attr)


if __name__ == '__main__':
    # create two instances
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1), s1.display())
    print(id(s2), s2.display())
