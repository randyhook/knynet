from simulator.bots.simbot import SimBot
from simulator.bots.sensors.simaudio import SimAudio

class GuardianBot(SimBot):
    '''A Guardian bot'''

    def __init__(self, serial_number, name, owner, subowners = None):
        '''Initialize the bot'''

        SimBot.__init__(self, serial_number, name, owner, subowners)

        self.sensors['audio'] = SimAudio(name = 'audio', brain = self.brain)
