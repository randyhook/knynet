class Goal():
    '''Base Goal class'''

    def __init__(self, spoken_language, time_processed):
        self.time_processed = time_processed
        self.encoded_message = spoken_language.encoded_message
        self.raw_message = spoken_language.raw_message
