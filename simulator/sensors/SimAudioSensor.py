from simulator.sensors.SimSensor import SimSensor
from environment.SensoryData import SensoryData

class SimAudioSensor(SimSensor):

    def __init__(self, parentBot, name):

        super().__init__('Audio', parentBot, name)
        
    def receiveAudio(self, audio):

        return SensoryData(self.name, 'Audio', audio)
