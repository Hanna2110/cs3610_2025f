from abc import ABC, abstractmethod

class ICruiseControlBehavior(ABC):
    '''
    Defining interface for cruise control functionality
    '''
    @abstractmethod
    def cruise_control(self):
        pass