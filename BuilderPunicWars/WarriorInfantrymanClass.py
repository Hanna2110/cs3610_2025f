from  BuilderPunicWars.IWarriorClass import IWarrior

class WarriorInfantryman(IWarrior):
    @staticmethod
    def info()-> None: 
        print("I am an Infantryman")