from utility.Observable import Observable

class Agent():

    def __init__(self, name, owner):

        self.name = name
        self.owner = owner

        self.memory = [];
        self.agencies = {}
        self.observable = Observable()

    def addAgency(self, agency):

        self.agencies[agency.name] = agency

    def hasAgency(self, agencyName):
        
        matchFound = False

        # rename passed in agency name to more general agency if appropriate
        if agencyName.lower() == 'weight':

            agencyName = 'physical'

        for a in list(self.agencies.keys()):

            if agencyName.lower() == a.lower():

                matchFound = True
                break;

        return matchFound

    def receiveSensoryData(self, data):

        if self.hasAgency(data.sensoryType):
           
            self.memory.append(self.agencies[data.sensoryType].processSensoryData(data))

            if data.sensoryType == 'Audio':

                if self.hasAgency('Language'):

                    self.observable.broadcast('Checking audio for language.')

                    languageEncoded = self.agencies['Language'].processSensoryData(data)

                    if languageEncoded is not None:

                        self.observable.broadcast('Language found. Processing.')

                        if self.agencies['Language'].isCommandToMe(languageEncoded, self.name):
                            self.observable.broadcast('This is a command to me.')

                        else:

                            self.observable.broadcast('This is not a command to me.')

            elif data.sensoryType == 'Weight':

                if self.hasAgency('Physical'):

                    self.observable.broadcast('Processing sensed weight.')
