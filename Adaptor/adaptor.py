class Target(object):
    """
    Target class with target interface
    """
    def behavior(self):
        return "Target: The default behaviour"
    

class Adaptee(object):
    """
    class wich we need to adapt to the target behavior
    """
    def adaptee_behavior(self):
        return "Adaptee"


class Adapter(Target):
    """
    makes adaptee interface work with target interface
    """

    def __init__(self, adaptee):
        self.adaptee = adaptee
    
    def behavior(self):
        return f"Adapter:  {self.adaptee.adaptee_behavior()[::-1]}"


class Client(object):
    """
    Client class works with Target interfaces
    """
    def __init__(self, target: Target):
        self.target = target
        print(target.behavior())

    
        


