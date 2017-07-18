from agency.Agency import Agency

class WheelchairAgency(Agency):

    def __init__(self, agent):

        self.name = 'Wheelchair'
        self.agent = agent

        self.isCarryingLoad = False

    def processSensoryData(self, data):

        if data.sensorName.lower() == 'seat':

            # testing: 10 is arbitrary
            if float(data.data) > 10:

                self.isCarryingLoad = True 

    def update(self):

        # if carrying load and TODO: visual sensor sees human in seat
        if self.isCarryingLoad:

            self.agent.belief.add('is-carrying-passenger', True)
