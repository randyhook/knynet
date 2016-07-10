class Bot:
    '''Base Bot class'''

    def __init__(self, name, serial_number, owner):
        '''Initialize a Bot'''

        self.serial_number = serial_number;
        self.name = name;
        self.owner = owner;

    def get_sensory_input():
        '''Query sensors for input from the outside world'''

    def power_up(self):
        '''Power up the bot'''
        pass

