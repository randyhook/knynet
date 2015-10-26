from abc import ABCMeta, abstractmethod

class Observable(object, metaclass=ABCMeta):

    def __init__(self):
        self.observers = list()

    @abstractmethod
    def attach_observer(self, observer):
        pass

    @abstractmethod
    def detach_observer(self, observer):
        pass

    @abstractmethod
    def notify_observer(self):
        pass
