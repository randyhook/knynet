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

    def update(self):
        
        audioSensor = self.hasSensor('Audio')

        if audioSensor is not None:

            rawAudio = self.sim.getRawAudio()

            if len(rawAudio) > 0:

                self.logStatusMessage(self.name + ': Receiving raw audio.')

                for a in rawAudio:

                    sData = audioSensor.receiveAudio(a)

                    self.agent.receiveSensoryData(sData)
