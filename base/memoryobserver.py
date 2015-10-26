from abc import ABCMeta, abstractmethod
from base.observer import Observer

class MemoryObserver(Observer):
    def update_from_observable(self):
        self.update_from_memory()

    @abstractmethod
    def update_from_memory(self):
        pass
