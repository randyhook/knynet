from agent.sensoryencoded.audioencoded import AudioEncoded

class SpokenLanguage(AudioEncoded):

    def __init__(self, raw_message, encoded_message, spoken_by):
        self.data_type = 'language'
        self.raw_message = raw_message
        self.encoded_message = encoded_message
        self.spoken_by = spoken_by
