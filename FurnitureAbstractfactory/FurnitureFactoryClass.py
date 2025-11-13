'''
The Abstract Factory Concrete Class
'''
from FurnitureAbstractfactory.IFurnitureFactoryClass import IFurnitureFactory
from FurnitureAbstractfactory.ChairFactoryClass import ChairFactory
from FurnitureAbstractfactory.TableFactoryClass import TableFactory

availableFurniture={'chair':ChairFactory, 'table':TableFactory}

class FurnitureFactory(IFurnitureFactory):
    
    @staticmethod
    def get_furniture(furniture):
        
        try:
            for k,v in availableFurniture.items():
                if k in furniture.lower():
                    print(furniture.lower())
                    if k=='chair':
                        #print("1")
                        return availableFurniture[k]().get_chair(furniture)
                    elif k=='table':
                        #print("2")
                        return availableFurniture[k].get_table(furniture)#!!! dif.implem. for Tables -> static
                    
                        
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None