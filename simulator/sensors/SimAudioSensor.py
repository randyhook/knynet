from simulator.sensors.SimSensor import SimSensor
from environment.SensoryData import SensoryData

class SimAudioSensor(SimSensor):

    def __init__(self, parentBot):

        super().__init__('Audio', parentBot)
        
    def receiveAudio(self, audio):

        return SensoryData('Audio', audio)
