from agency.Agency import Agency
from environment.AudioEncoded import AudioEncoded

class AudioAgency(Agency):

    def __init__(self, agent):

        self.name = 'Audio'
        self.agent = agent

    def processSensoryData(self, data):
        return AudioEncoded()
