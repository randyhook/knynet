from bots.brain.brain import Brain
from simulator.events.audioevent import AudioEvent

class SimBrain(Brain):
    '''Brain for SimBot'''

    def __init__(self, serial_number, name, owner, subowners, chain_of_command):

        self.name = name
        self.serial_number = serial_number
        self.owner = owner
        self.subowners = subowners
        self.chain_of_command = chain_of_command

        self.sensory_input_queue = list()
        self.sensory_encoded_history = list()

        self.agencies = dict()
        self.standing_orders = list()

    def process_sensory_input(self):
        '''Override for Bot.Brain.process_sensory_input() since here we are dealing with events instead of SensoryData'''

        for i in self.sensory_input_queue:
            if (isinstance(i, AudioEvent)):
                if ('audio' in self.agencies):
                    self.process_sensory_encoded(self.agencies['audio'].process(i))

    def queue_sensory_input(self, event):
        '''Override for Bot.Brain.queue_sensory_input() since here we are accepting an event instead of SensoryData'''

        self.sensory_input_queue.append(event)

        self.process_sensory_input()

        return []

