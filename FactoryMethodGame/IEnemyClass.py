from abc import ABC, abstractmethod

'''The Enemy Interface (Product)'''

class IEnemy(ABC):
    
    @staticmethod
    @abstractmethod
    def attack()-> None: #A static interface method
        pass