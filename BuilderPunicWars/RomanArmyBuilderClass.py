from BuilderPunicWars.IBuilderClass import IBuilber
from BuilderPunicWars.ArmyClass import Army
from BuilderPunicWars.WarriorInfantrymanClass import WarriorInfantryman
from BuilderPunicWars.WarriorHorsemanClass import WarriorHorseman
from BuilderPunicWars.CombatUnit_CatapultClass import CombatUnit_Catapult

class RomanArmyBuilder(IBuilber):
    
    def __init__(self) -> None:
        self.reset()
        
    def reset(self) -> None:
        self.__product = Army("Roman Army")
        
    @property
    def product(self) -> None:#getResult method --> Army
        currentProduct=self.__product
        self.reset()#ready to start producing another product
        return currentProduct

    def buildArcher(self) -> None:
        pass

    def buildHorseman(self) -> None:
        self.__product.add(WarriorHorseman())

    def buildElephant(self) -> None:
        pass
        
    def buildInfantryman(self) -> None:
        self.__product.add(WarriorInfantryman())
    
    def buildCatapult(self) -> None:
        self.__product.add(CombatUnit_Catapult())

