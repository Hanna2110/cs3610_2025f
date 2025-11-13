from FurnitureAbstractfactory.IChairClass import IChair

'''
The Small Chair Concrete Class implements the IChair interface
'''
class SmallChair(IChair):  
    def __init__(self):
        #print("i am a Small Chair")
        self.__height = 40
        self.__width = 40
        self.__depth = 40

    def get_dimensions(self):
        return {
            "width": self.__width,
            "depth": self.__depth,
            "height": self.__height
        }