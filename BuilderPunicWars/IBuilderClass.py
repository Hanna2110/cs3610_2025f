from abc import ABC, abstractmethod

class IBuilber(ABC):
    @property
    @abstractmethod
    def product(self) -> None:#getResult method --> Army
        pass

    @abstractmethod
    def buildArcher(self) -> None:
        pass

    @abstractmethod
    def buildHorseman(self) -> None:
        pass

    @abstractmethod
    def buildInfantryman(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def buildElephant(self) -> None:
        pass

    @abstractmethod
    def buildCatapult(self) -> None:
        raise NotImplementedError