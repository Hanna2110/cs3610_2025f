from FactoryMethodGame.EasyLevelClass import EasyLevel
from FactoryMethodGame.HardLevelClass import HardLevel

def gameWithLevels():
    easyLevel= EasyLevel()
    print("The easy level started!")
    easyLevel.startGame()
    
    hardLevel= HardLevel()
    print("The hard level started!")
    hardLevel.startGame()
    