from FactoryMethodGame.IEnemyClass import IEnemy

'''
The Vampire Concrete Class implements the IEnemy interface
'''
class Vampire(IEnemy):  
    def __init__(self):
        self.__name = "My Vampire"

    def attack(self):
        return f"{self.__name} is attacking now..."