from bots.brain.agencies.audioagency import AudioAgency
from bots.brain.sensoryencoded.spokenlanguage import SpokenLanguage
from simulator.events.audioevent import AudioEvent

class SimAudioAgency(AudioAgency):

    def process_sensory_data(self, sensory_data):
        '''Process an simulated audio sensory data'''

        #TODO: determine if language is contained in sensory_data
