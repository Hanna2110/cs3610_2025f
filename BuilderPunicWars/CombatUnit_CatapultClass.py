from BuilderPunicWars.ICombatUnitClass import ICombatUnit

class CombatUnit_Catapult(ICombatUnit):
    @staticmethod
    def data()-> None: 
        print("This is a Catapult")