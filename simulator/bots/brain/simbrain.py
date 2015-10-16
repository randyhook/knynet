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

        self.sensory_data_queue = list()

        self.agencies = dict()
        self.standing_orders = list()

    def process_sensory_data_queue(self):
        '''Override for Bot.Brain.process_sensory_data_queue() since here we are dealing with SimSensoryData instead of SensoryData'''

        messages = list();

        for s in self.sensory_data_queue:
            if (s.data == 'audio'):
                if ('audio' in self.agencies):
                    for m in self.agencies['audio'].process_sensory_data(s):
                        messages.append(m)

        return messages

    def queue_sensory_data(self, sd):
        '''Override for Bot.Brain.queue_sensory_data() since here we are accepting an SimSensoryData instead of SensoryData'''

        self.sensory_data_queue.append(sd)

        return []

