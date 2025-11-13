from FactoryMethodGame.IEnemyClass import IEnemy


from typing import Type
from abc import abstractmethod


class GameLevel:
    def __init__(self) -> None:
        self._enemies: list[Type[IEnemy]]=[]
        
    @abstractmethod
    def createEnemies() -> None:
        pass
    
    def startGame(self) -> None:
        self.createEnemies()
        #print(len(self._enemies))
        for myEnemy in self._enemies:
            print(myEnemy.attack())
        