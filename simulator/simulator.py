import random
from simulator.bots.simbot import SimBot
from simulator.simhuman import SimHuman

class Simulator():
    '''Simulator class'''

    def __init__(self):
        '''Initialize the simulator'''

        self.humans = dict()
        self.bots = dict()

        # create the bots
        new_serial_number = self.get_unique_serial_number()
        randy = SimHuman.create(new_serial_number, 'Randy', 'Hook')
        self.humans[randy.serial_number] = randy

        # create the humans
        new_serial_number = self.get_unique_serial_number()
        guardianbot = SimBot.create('Guardianbot', new_serial_number, self.humans[randy.serial_number])
        self.bots[guardianbot.serial_number] = guardianbot

        self.start_simulation()

    def get_simulator_command(self, input_string):
        '''Get the command portion of the user input'''

        parts = input_string.split(' ')

        if len(parts) == 0:
            return ''
        else:
            return parts[0].lower()

    def get_unique_serial_number(self):
        '''Generate a unique serial number'''
        #
        # returns a unique number or -1 on failure

        # seed the randomizer
        random.seed()

        # prepare the loop
        new_serial_number = -1
        unique_generated = False
        current_try = 1
        max_tries = 800000

        # generate numbers until we hit the maximum allowable tries
        while unique_generated == False and current_try < max_tries:
            new_serial_number = random.randint(100000, 900000)

            # check if any bot already has this number
            match_found = False
            for b in self.bots:
                if b.serial_number == new_serial_number:
                    match_found = True
                    break

            # if not matches were found, we've got a unique number
            if match_found == False:
                unique_generated = True

            # set the serial number back to -1 if we've exhausted our tries
            if ++current_try >= max_tries:
                new_serial_number = -1

        return new_serial_number

    def start_simulation(self):
        '''Start the simulation'''

        current_input = ''

        while current_input.lower() != 'quit':
            current_input = input('-->')

            current_command = self.get_simulator_command(current_input)
