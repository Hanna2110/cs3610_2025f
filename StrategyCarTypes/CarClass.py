class Car:
    '''
    Base class for car types
    '''
    
    def __init__(self) -> None:
        self._cruise_control_strategy = None
        self._drive_strategy = None
        self._moon_roof_strategy = None
        
    @property
    def cruise_control_strategy(self):
        return self._cruise_control_strategy

    @cruise_control_strategy.setter
    def cruise_control_strategy(self, cruise_control_strategy):
        self._cruise_control_strategy = cruise_control_strategy

    @property
    def drive_strategy(self):
        return self._cruise_control_strategy

    @drive_strategy.setter
    def drive_strategy(self, drive_strategy):
        self._drive_strategy = drive_strategy

    @property
    def moon_roof_strategy(self):
        return self._moon_roof_strategy

    @moon_roof_strategy.setter
    def moon_roof_strategy(self, moon_roof_strategy):
        self._moon_roof_strategy = moon_roof_strategy
        
        
    def assemble(self, cruise_control_strategy,drive_strategy,moon_roof_strategy=None):
        self._cruise_control_strategy = cruise_control_strategy
        self._drive_strategy = drive_strategy
        self._moon_roof_strategy = moon_roof_strategy
        print("car is ready now")
        
    def drive(self):
        self._drive_strategy.drive()
        
    def cruise_controlON(self):
        self._cruise_control_strategy.cruise_control()
        
    def moon_roofON(self):
        self._moon_roof_strategy.moon_roof()