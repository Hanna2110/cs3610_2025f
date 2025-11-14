from abc import ABC, abstractmethod

class IWarrior(ABC):
    @staticmethod
    @abstractmethod
    def info()-> None: 
        pass