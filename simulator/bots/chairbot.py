from bots.brain.agencies.navigatoragency import NavigatorAgency
from simulator.bots.simbot import SimBot
from simulator.bots.sensors.simaudio import SimAudio

from simulator.bots.brain.agencies.simnaturallanguageagency import SimNaturalLanguageAgency
from simulator.bots.brain.agencies.simaudioagency import SimAudioAgency

class ChairBot(SimBot):
    '''A wheelchair bot'''

    def __init__(self, serial_number, name, owner, subowners = None):
        '''Initialize the bot'''

        SimBot.__init__(self, serial_number, name, owner, subowners)

        self.brain.agencies['audio'] = SimAudioAgency(self.brain)
        self.brain.agencies['natural_language'] = SimNaturalLanguageAgency(self.brain)
        self.brain.agencies['navigator'] = NavigatorAgency()

        self.passenger = None
        self.sensors['audio'] = SimAudio(name = 'audio', brain = self.brain)
