from StrategyCarTypes.IDriveBehaviorClass import IDriveBehavior

class ElectricDrive(IDriveBehavior):
    def drive(self):
        print("I provide Electric Drive")