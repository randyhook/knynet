from bot.Bot import Bot
from agent.Agent import Agent
from environment.SensoryData import SensoryData
from utility.Observer import Observer

class SimBot(Bot):
    ''' Bot for Simulator '''

    def __init__(self, sim, name, owner):

        super().__init__(name, owner)

        self.sensors = []
        self.sim = sim

        self.observer = Observer(self.notify)
        self.agent.observable.attachObserver(self.observer)

    def addSensor(self, newSensor):

        self.sensors.append(newSensor)

    def hasSensor(self, sensorType):

        for s in self.sensors:

            if s.sensorType == sensorType:

                return s

        return None

    def logStatusMessage(self, msg):

        self.sim.addStatusMessage(msg)

    def notify(self, msg):
        
        self.logStatusMessage(msg)

    def receiveStimuli(self, stimuli):

        terms = stimuli.split(' ')

        if len(terms) < 2:
            return

        for s in self.sensors:

            if s.sensorType.lower() == terms[0].lower():
                
                if terms[0].lower() == 'weight':
                    
                    self.logStatusMessage(self.name + ': Sensing weight.')

                    sData = s.receiveWeight(terms[1])

                    self.agent.receiveSensoryData(sData)

    def updateFromEnvironment(self):
        
        envAudio = self.sim.getEnvAudio()

        for s in self.sensors:

            if s.sensorType == 'Audio':

                if len(envAudio) > 0:

                    self.logStatusMessage(self.name + ': Sensing audio.')

                for a in envAudio:

                    sData = s.receiveAudio(a)

                    self.agent.receiveSensoryData(sData)
