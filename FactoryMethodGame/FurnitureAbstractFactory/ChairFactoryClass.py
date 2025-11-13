from FurnitureAbstractfactory import SmallChairClass, BigChairClass
from FurnitureAbstractfactory.IChairClass import IChair


'''
Each concrete factory corresponds to a specific product variant
'''


class ChairFactory:  
    '''
    The Concrete Chair Factory Class
    '''
    def __init__(self):
        #print("@@@@")
        self.__chairTypes={'smallchair':SmallChairClass.SmallChair, 'bigchair':BigChairClass.BigChair}

    def get_chair(self, chair:str)-> IChair:
        '''A static method to get a table'''
        if chair.lower() in self.__chairTypes:
            #print("Thanks for the Chair!")
            return self.__chairTypes[chair]()
        else:
            print(f"Chair {chair} Not Found")
            return None
        