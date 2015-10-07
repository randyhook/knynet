from bots.brain.agencies.audioagency import AudioAgency
from bots.brain.sensoryencoded.spokenlanguage import SpokenLanguage
from simulator.events.audioevent import AudioEvent

class SimAudioAgency(AudioAgency):

    def process(self, audio_event):
        '''Process an AudioEvent. This differs from the real AudioAgency which processes SensoryData'''

        if (audio_event.audio_type == 'voice'):
            return(SpokenLanguage(audio_event.audio_data, audio_event.initiator))
