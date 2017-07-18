from agency.Agency import Agency
from environment.PhysicalEncoded import PhysicalEncoded

class PhysicalAgency(Agency):

    def __init__(self, agent):

        self.name = 'Physical'
        self.agent = agent

    def processSensoryData(self, data):
        
        pass
