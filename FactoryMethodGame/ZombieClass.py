from FactoryMethodGame.IEnemyClass import IEnemy

'''
The Zombie Concrete Class implements the IEnemy interface
'''
class Zombie(IEnemy):  
    def __init__(self):
        self.__name = "My Zombie"

    def attack(self):
        return f"{self.__name} is attacking now..."