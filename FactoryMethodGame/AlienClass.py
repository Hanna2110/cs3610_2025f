from FactoryMethodGame.IEnemyClass import IEnemy


'''
The Alien Concrete Class implements the IEnemy interface
'''
class Alein(IEnemy):  
    def __init__(self):
        self.__name = "My Alein"

    def attack(self):
        return f"{self.__name} is attacking now..."