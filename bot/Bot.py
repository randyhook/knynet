from agent.Agent import Agent

class Bot:
    ''' Base Bot class intended for use in hardware '''

    def __init__(self, name, owner):

        self.agent = Agent(name, owner)

        self.name = name
        self.owner = owner

    def updateInternalState(self):

        if self.agent.specializedAgency is not None:

            self.agent.agencies[self.agent.specializedAgency].update()
