from FactoryMethodGame.IEnemyClass import IEnemy

'''
The Robot Concrete Class implements the IEnemy interface
'''
class Robot(IEnemy):  
    def __init__(self):
        self.__name = "My Robot"

    def attack(self):
        return f"{self.__name} is attacking now..."