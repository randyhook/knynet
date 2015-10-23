class SensoryEncoded():
    '''Base class for encoded sensory data
        This class is used to transform raw SensoryData into something usable'''

    def __init__(self):
        self.encoded_message = None
        self.origin = None
