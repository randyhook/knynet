from base.observable import Observable
from base.observablenotification import ObservableNotification
from datetime import datetime

class Memory(Observable):
    '''Base Memory class'''

    def __init__(self, agent):
        self.observers = list()
        self.agent = agent
        self.sensory_encoded_storage = list()
        self.action_log = list()

    def attach_observer(self, observer):
        self.observers.append(observer)

    def detach_observer(self, observer):
        pass

    def notify_observer(self, notification):
        for o in self.observers:
            o.update_from_observable(notification)

    def store_action(self, message):
        self.action_log.append((datetime.now(), message))
        self.notify_observer(ObservableNotification(self.agent.name, 'store_action', message))

    def store_sensory_encoded(self, data):
        self.sensory_encoded_storage.append((datetime.now(), data))
        self.notify_observer(ObservableNotification(self.agent.name, 'store_sensory_encoded', data.raw_message))
