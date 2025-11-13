from FactoryMethodGame.IEnemyClass import IEnemy
from FactoryMethodGame.AlienClass import Alein
from FactoryMethodGame.RobotClass import Robot
from FactoryMethodGame.VampireClass import Vampire
from FactoryMethodGame.ZombieClass import Zombie

class EnemyFactory:
    @staticmethod
    def createEnemy(objType: str) ->IEnemy: #A static method to get a concrete product
        try:
            if objType.lower()=='alein':
                return Alein()
            elif objType.lower()=='robot':
                return Robot()
            elif objType.lower()=='vampire':
                return Vampire()
            elif objType.lower()=='zombie':
                #print("I am making a Zombie..")
                return Zombie()
            else:
                raise Exception(f"I can't make this enemy {objType}")
        except Exception as _e:
            print(_e)
        return None
    