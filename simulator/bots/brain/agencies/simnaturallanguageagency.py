from bots.brain.agencies.naturallanguageagency import NaturalLanguageAgency
import bots.brain.agencies.nltk

class SimNaturalLanguageAgency(NaturalLanguageAgency):

    def __init__(self, brain):
       self.brain = brain

    def containsLanguage(self, data):
        '''Check if audio data contains language'''

        return True

    def process_sensory_data(self, sensory_data):
        '''Process simulated audio sensory data'''

        messages = list()

        if self.containsLanguage(sensory_data.data):
            #print(nltk.word_tokenize(sensory_data.data))
            pass

        return messages
