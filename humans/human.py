from base.tangible import Tangible

class Human(Tangible):
    '''Base class for humans'''

    def __init__(self, serial_number, first_name, last_name):
        '''Initialize a Human'''

        if len(first_name) == 0 or len(last_name) == 0:
            raise ValueError('A human must have a first and last name')

        self.first_name = first_name
        self.last_name = last_name
        self.serial_number = serial_number

