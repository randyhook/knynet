from simulator.events.simevent import SimEvent

class AudioEvent(SimEvent):
    '''Audio Event class'''

    def __init__(self, initiator, audio_type, audio_data):
        '''Initialize the audio event'''

        self.initiator = initiator
        self.audio_type = audio_type
        self.audio_data = audio_data
