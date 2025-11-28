from abc import ABC, abstractmethod

class IDriveBehavior(ABC):
    '''
    Defining interface for drive functionality of car
    '''
    @abstractmethod
    def drive(self):
        pass