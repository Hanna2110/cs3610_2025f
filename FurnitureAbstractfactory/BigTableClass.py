from FurnitureAbstractfactory.ITableClass import ITable

'''
The Small Table Concrete Class implements the IChair interface
'''
class BigTable(ITable):  
    def __init__(self):
        self.__height = 70
        self.__width = 150
        self.__depth = 50

    def get_dimensions(self):
        return {
            "width": self.__width,
            "depth": self.__depth,
            "height": self.__height
        }