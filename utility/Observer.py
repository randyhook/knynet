class Observer:

    def __init__(self, notifyFunc):

        self.notifyFunc = notifyFunc

    def notify(self, msg):
        
        self.notifyFunc(msg)
