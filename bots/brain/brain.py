from bots.brain.sensoryencoded.sensoryencoded import SensoryEncoded
from bots.brain.sensoryencoded.audioencoded import AudioEncoded
from bots.brain.sensoryencoded.spokenlanguage import SpokenLanguage

class Brain:
    '''Base Brain class for Bot'''

    def __init__(self, name, serial_number, owner, subowners, chain_of_command):

        self.update_delta_milliseconds = 100

        self.name = name
        self.serial_number = serial_number
        self.owner = owner
        self.subowners = subowners
        self.chain_of_command = chain_of_command
    
        self.sensory_data_queue = list()

        self.agencies = dict()
        self.standing_orders = list()

    def process_sensory_data(self):
        pass

    def process_sensory_encoded(self, sensory_encoded):
        if isinstance(sensory_encoded, SpokenLanguage):
            if 'natural_language' in self.agencies:
                self.store_knowledge(self.agencies['natural_language'].process(sensory_encoded.encoded_message, sensory_encoded.spoken_by))

    def queue_sensory_data(self, sd):
        pass
