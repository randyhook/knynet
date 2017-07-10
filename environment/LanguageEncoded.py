from environment.SensoryEncoded import SensoryEncoded

import nltk

class LanguageEncoded(SensoryEncoded):

    def __init__(self, data):
        
        self.rawData = data

        self.tokens = nltk.word_tokenize(self.rawData)
