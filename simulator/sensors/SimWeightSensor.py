from simulator.sensors.SimSensor import SimSensor
from environment.SensoryData import SensoryData

class SimWeightSensor(SimSensor):

    def __init__(self, parentBot):

        super().__init__('Weight', parentBot)
        
    def receiveWeight(self, grams):

        return SensoryData('Weight', grams)
