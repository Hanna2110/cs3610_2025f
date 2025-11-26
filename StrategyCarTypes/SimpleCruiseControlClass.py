from StrategyCarTypes.ICruiseControlBehaviorClass import ICruiseControlBehavior

class SimpleCruiseControl(ICruiseControlBehavior):
    '''
    Algorithm #2: regular cruise control.
    '''
    def cruise_control(self):
        print("Regular cruise control")