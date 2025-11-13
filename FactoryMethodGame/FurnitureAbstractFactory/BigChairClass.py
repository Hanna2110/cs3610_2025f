from FurnitureAbstractfactory.IChairClass import IChair

'''
The Big Chair Concrete Class implements the IChair interface
'''
class BigChair(IChair):  
    def __init__(self):
        self.__height = 90
        self.__width = 90
        self.__depth = 90

    def get_dimensions(self):
        return {
            "width": self.__width,
            "depth": self.__depth,
            "height": self.__height
        }