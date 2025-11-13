from abc import ABC, abstractmethod

'''The Chair Interface (Product)'''

class IChair(ABC):
    
    @staticmethod
    @abstractmethod
    def get_dimensions()-> None: #A static interface method
        pass