from agency.Agency import Agency
from environment.VisualEncoded import VisualEncoded

class VisualAgency(Agency):

    def __init__(self, agent):

        self.name = 'Visual'
        self.agent = agent
