from BuilderPunicWars.IWarriorClass import IWarrior
from BuilderPunicWars.ICombatUnitClass import ICombatUnit

class Army:
    def __init__(self, name: str) -> None:
        self.__name=name
        self.__warriors = []
        self.__combatUnits= []
        
    def add(self, component) -> None:
        if isinstance(component, IWarrior):
            self.__warriors.append(component)
            #print(self.__warriors)
        elif isinstance(component, ICombatUnit):
            self.__combatUnits.append(component)
            #print(self.__combatUnits)
        
    def showComponents(self) -> None:
        print(f"There is/are {len(self.__warriors)+len(self.__combatUnits)} element(s) in the {self.__name} army.")
        
        if len(self.__warriors)>0:
            print(f"The warriors of {self.__name} Army are:")
            for item in self.__warriors:
                item.info()
                
        if len(self.__combatUnits)>0:
            print(f"The warriors of {self.__name} Army are:")
            for item in self.__combatUnits:
                item.data()