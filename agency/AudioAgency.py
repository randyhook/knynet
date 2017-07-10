from agency.Agency import Agency
from environment.AudioEncoded import AudioEncoded

class AudioAgency(Agency):

    def __init__(self):
        self.name = 'Audio'

    def processSensoryData(self, data):
        return AudioEncoded()
