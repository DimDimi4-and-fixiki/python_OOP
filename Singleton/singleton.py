class MetaSingleton(type):
    """
    Metaclass for singleton
    """

    def __init__(self, **kwargs):
        _instance = kwargs.get("instance", None)

    def __call__(self) -> Singleton:
        if self._instance == None:
            self.instance = super().__call__()
        return self._instance
    
class Singleton(metaclass=MetaSingleton):

    def logic(self):
        """
        logic in Singleton for an instance 
        """
        pass

