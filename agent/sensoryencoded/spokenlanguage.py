from agent.sensoryencoded.audioencoded import AudioEncoded

class SpokenLanguage(AudioEncoded):

    def __init__(self, message, spoken_by):
        self.data_type = 'language'
        self.encoded_message = message
        self.spoken_by = spoken_by
