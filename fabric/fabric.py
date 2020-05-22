class Creator(object):


    def method(self):
        """
        method of fabric
        """
        pass
    
    def operation(self):
        
        product = self.method()
        result = "It works with{}".format(product)
        return result 


class Creator1(Creator):
    """
    creator object with its methods
    """

    def method(self):
        return Product1()


class Product(object):
    """
    Abstract product
    """
    def operation(self):
        pass


class Product1(Product):
    """
    Product object with its method
    """
    def operation(self):
        return "{Result of product1}"


class Client(object):
    """
    Client interface
    """
    def __init__(self, creator):
        self.creator = creator
        print("Client: {}".format(self.creator.operation()))

"""
if __name__ == "__main__":
    print("Creator1")
    client = Client(Creator1())
"""


