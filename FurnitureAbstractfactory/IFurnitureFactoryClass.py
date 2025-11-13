from abc import ABC, abstractmethod

#Abstract Interface for Furniture Factory 

class IFurnitureFactory(ABC):
    

    @staticmethod
    @abstractmethod
    def get_furniture(furniture) -> None: #The static Abstract factory interface method
        pass
        