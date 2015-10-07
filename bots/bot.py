from humans.human import Human
from bots.brain.brain import Brain

class Bot:
    '''Base Bot class'''

    def __init__(self, serial_number, name, owner, subowners, chain_of_command):
        '''Initialize a Bot'''

        if (len(str(name)) == 0):
            raise ValueError('A Bot must be initialized with a name');

        if not isinstance(owner, Human):
            raise TypeError('Owner of a Bot must be a Human')

        if (len(str(serial_number)) == 0):
            raise ValueError('A Bot must be initialized with a serial number')

        self.brain = Brain(serial_number, name, owner, subowners, chain_of_command)
        self.sensors = dict()

    def get_sensory_input():
        '''Query sensors for input from the outside world'''

    def power_up(self):
        '''Power up the bot'''
        pass

