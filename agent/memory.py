class Memory():
    '''Base Memory class'''

    def __init__(self):
        self.encoded_storage = list()

    def store(self, encoded):
        self.encoded_storage.append(encoded)
