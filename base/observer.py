from abc import ABCMeta, abstractmethod

class Observer(object, metaclass=ABCMeta):
    @abstractmethod
    def update_from_observable(self):
        pass
