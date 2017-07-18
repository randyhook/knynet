from environment.SensoryEncoded import SensoryEncoded

class Belief():

    def __init__(self):

        self.statements = []

    def add(self, statement, value):

        self.statements.append((statement, value))
