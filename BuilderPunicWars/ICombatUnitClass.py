from abc import ABC, abstractmethod

class ICombatUnit(ABC):
    @staticmethod
    @abstractmethod
    def data()-> None: 
        pass