from base.observable import Observable
from datetime import datetime

class Memory(Observable):
    '''Base Memory class'''

    def __init__(self):
        self.sensory_encoded_storage = list()
        self.action_log = list()

    def attach(self, observer):
        pass

    def detach(self, observer):
        pass

    def store_action(self, message):
        self.action_log.append((datetime.now(), message))

    def store_sensory_encoded(self, data):
        self.sensory_encoded_storage.append((datetime.now(), data))
