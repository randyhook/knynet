from agency.Agency import Agency
from environment.PhysicalEncoded import PhysicalEncoded

class PhysicalAgency(Agency):

    def __init__(self):
        self.name = 'Physical'

    def processSensoryData(self, data):
        return PhysicalEncoded(data.sensoryType, data)
