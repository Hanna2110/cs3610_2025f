from FactoryMethodGame.GamaLevelClass import GameLevel
from FactoryMethodGame.EnemyFactoryClass import EnemyFactory


class HardLevel(GameLevel):
    def __init__(self) -> None:
        super().__init__()
        
    def createEnemies(self) -> None:
        enemies=['ZOMBIE','RoboT','vampirE','VAMPIRE1']
        myEnemies=list(map(EnemyFactory.createEnemy,enemies))
        #print(len(myEnemies))
        
        for myEnemy in myEnemies:
            if myEnemy:
                self._enemies.append(myEnemy)