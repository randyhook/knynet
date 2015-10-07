from simulator.utils import Utils
from simulator.room import Room

class World:
    '''A class for the simulation's world'''

    def __init__(self):
        '''Initialize the simulated world'''

        # keep track of all the serial numbers in the world so we don't duplicate any
        self.serial_numbers = []

        self.rooms = dict({'living_room': Room('Living Room')})

    def generate_new_serial_number(self):
        '''Generate a new serial number and verify it is unique'''

        new_serial_number = ''
        while (new_serial_number == ''):
            new_serial_number = Utils.get_random_serial_number()

            if (new_serial_number in self.serial_numbers):
                new_serial_number = ''

        self.serial_numbers.append(new_serial_number)
        return new_serial_number
