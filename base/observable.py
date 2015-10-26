from abc import ABCMeta, abstractmethod

class Observable(object, metaclass=ABCMeta):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass
