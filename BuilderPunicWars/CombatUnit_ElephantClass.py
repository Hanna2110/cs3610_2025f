from BuilderPunicWars.ICombatUnitClass import ICombatUnit

class CombatUnit_Elephant(ICombatUnit):
    @staticmethod
    def data()-> None: 
        print("This is a Elephant")