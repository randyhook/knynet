from agent.agencies.audioagency import AudioAgency

class SimAudioAgency(AudioAgency):

    def __init__(self, agent):
       self.agent = agent

    @classmethod
    def audio_contains_language(cls, sensory_data):
        '''Determine if audio sensory data contains language'''

        #stub
        return True

    def process_sensory_data(self, sensory_data):
        '''Process an simulated audio sensory data'''

        messages = list()

        if SimAudioAgency.audio_contains_language(sensory_data):
            if 'natural_language' in self.agent.agencies:
                for m in self.agent.agencies['natural_language'].process_sensory_data(sensory_data):
                    messages.append(m)

        return messages
