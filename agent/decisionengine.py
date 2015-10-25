class DecisionEngine():
    '''Base Decision Engine class'''

    def __init__(self, agent):
        self.agent = agent

    def i_am_being_addressed(self, message):
        return True

    def process_sensory_encoded(self, encoded):
        if (encoded.data_type == 'language'):
            if (self.i_am_being_addressed(encoded.encoded_message)):
                print('acknowledged')
