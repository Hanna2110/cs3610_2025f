from typing import Type
from BuilderPunicWars.IBuilderClass import IBuilber

class ArmyDirector:
    def __init__(self) -> None:
        self.__builder = None

    @property
    def builder(self) -> IBuilber:
        return self.__builder

    @builder.setter
    def builder(self, builder: Type[IBuilber]) -> None:
        self.__builder=builder
        
    def makeArmy(self)-> None:
        self.builder.buildArcher()
        self.builder.buildHorseman()
        self.builder.buildInfantryman()
        self.builder.buildElephant()
        self.builder.buildCatapult()
        
        self.builder.product.showComponents()