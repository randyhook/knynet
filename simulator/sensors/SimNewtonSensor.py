from simulator.sensors.SimSensor import SimSensor
from environment.SensoryData import SensoryData

class SimNewtonSensor(SimSensor):

    def __init__(self, parentBot, name):

        super().__init__('Newton', parentBot, name)
        
    def receiveWeight(self, value):

        return SensoryData(self.name, 'newton', value)
