from BuilderPunicWars.ArmyDirectorClass import ArmyDirector
from BuilderPunicWars.CarthaginianArmyBuilderClass import CarthaginianArmyBuilder
from BuilderPunicWars.RomanArmyBuilderClass import RomanArmyBuilder

def PunicsWarsGame():
    gameDirector=ArmyDirector()
    
    romanBuilder = RomanArmyBuilder()
    gameDirector.builder=romanBuilder
    print("The Roman Army.")
    gameDirector.makeArmy()

    carthaginianBuilder=CarthaginianArmyBuilder()
    gameDirector.builder=carthaginianBuilder
    print("The Carthaginian Army.")
    gameDirector.makeArmy()
    