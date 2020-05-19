class Director(object):
    """
    Director class 
    Describes the order of builders tasks
    """
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder
    
    def get_object(self):
        """
        creating object
        specifing this object with builder methods
        """
        obj = Object()

        param1 = self.__builder.get1()
        obj.set1(param1)

        param2 = self.__builder.get2()
        obj.set2(param2)

        param3 = self.__builder.get3()
        obj.set3(param3)

        return obj


class Object(object):
    """
    An abstract object
    """
    def __init__(self):
        self.param1 = None
        self.param2 = None
        self.param3 = None
    
    def set1(self, param1):
        self.param1 = param1
    
    def set2(self, param2):
        self.param2 = param2
    
    def set3(self, param3):
        self.param3 = param3


class Builder(object):
    """
    General Builder class
    """
    def get1(self):
        pass
    
    def get2(self):
        pass
    
    def get3(self):
        pass

class ObjectBuilder(Builder):
    """
    Builder for Object class
    """
    @staticmethod
    def get1():
        return 1

    @staticmethod
    def get2():
        return 2

    @staticmethod
    def get3():
        return 3

def main():
    obj_builder = ObjectBuilder() # initializing onject builder
    director = Director()

    director.setBuilder(obj_builder) # setting the builder we need
    obj = director.get_object() # getting the object from director
