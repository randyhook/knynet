class Observable:

    def __init__(self):

        self.observers = []

    def attachObserver(self, obs):
        
        self.observers.append(obs)

    def broadcast(self, msg):
        
        for o in self.observers:

            o.notify(msg)
