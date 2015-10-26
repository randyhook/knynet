from agent.agencies.naturallanguageagency import NaturalLanguageAgency
import nltk

from agent.sensoryencoded.spokenlanguage import SpokenLanguage

class SimNaturalLanguageAgency(NaturalLanguageAgency):

    def __init__(self, agent):
       self.agent = agent

    def containsLanguage(self, data):
        '''Check if audio data contains language'''

        return True

    def process_sensory_data(self, sensory_data):
        '''Process simulated audio sensory data'''

        if self.containsLanguage(sensory_data.data):
            tokens = nltk.word_tokenize(sensory_data.data)
            pos = nltk.pos_tag(tokens)

            return(SpokenLanguage(raw_message = sensory_data.data, encoded_message = pos, spoken_by = sensory_data.origin))
