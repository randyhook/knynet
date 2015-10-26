from agent.memory import Memory
import nltk

class DecisionEngine():
    '''Base Decision Engine class'''

    def __init__(self, agent):
        self.agent = agent

    def i_am_being_addressed(self, message):
        # for each word in the agent's name
        name_part_counter = 0
        for name_part in self.agent.name.split(' '):

            # check if name part matches same position in message
            if (name_part_counter < len(message) and name_part.lower() != message[name_part_counter][0].lower()):
                return False

            name_part_counter = name_part_counter + 1

        # check if the message still has addressee components, if it does, the agent being addressed has a longer name than this one.
        if message[name_part_counter][0] not in ['.', ',', '!']:
            return False

        return True

    def process_language(self, encoded):
        if (self.i_am_being_addressed(encoded.encoded_message)):
            # TODO: check if this is a command, and if so, if addresser has the authority to issue command to this agent
            self.agent.memory.store_action(self.agent.name + ' acknowledging.')

    def process_sensory_encoded(self, encoded):
        # store the data to memory
        self.agent.memory.store_sensory_encoded(encoded) 

        # process the data into knowledge
        if (encoded.data_type == 'language'):
            self.process_language(encoded)
