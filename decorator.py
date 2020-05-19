"""
DECORATOR OOP PATTERN
"""

class Component():

    """
    base insterface with some methods and base behaviour
    """

    def method():
        pass

class Decorator(Component):
    """
    base decorator class
    """

    def __init__(self, component):
        self._component = component
    
    @property
    def component(self):
        return self._component
    
    def operation(self):
        return self._component.method()

