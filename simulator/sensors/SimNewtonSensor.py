from simulator.sensors.SimSensor import SimSensor
from environment.SensoryData import SensoryData

class SimNewtonSensor(SimSensor):

    def __init__(self, parentBot):

        super().__init__('Newton', parentBot)
        
    def receiveWeight(self, value):

        return SensoryData('newtons', value)
