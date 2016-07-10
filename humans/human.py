from base.tangible import Tangible

class Human(Tangible):
    '''Base class for humans'''

    def __init__(self, serial_number, first_name, last_name):
        '''Initialize a Human'''

        self.first_name = first_name
        self.last_name = last_name
        self.serial_number = serial_number
