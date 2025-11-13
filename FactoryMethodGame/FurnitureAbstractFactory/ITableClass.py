from abc import ABC, abstractmethod

'''The Table  Interface (Product)'''

class ITable(ABC):
    
    @staticmethod
    @abstractmethod
    def get_dimensions()-> None: #A static interface method
        pass