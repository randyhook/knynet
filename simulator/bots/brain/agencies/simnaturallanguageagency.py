from bots.brain.agencies.naturallanguageagency import NaturalLanguageAgency

class SimNaturalLanguageAgency(NaturalLanguageAgency):

    def __init__(self, brain):
       self.brain = brain

    def process_sensory_data(self, sensory_data):
        '''Process simulated audio sensory data'''

        messages = list()

        return messages
