import random

class Utils:
    '''Utility class for the simulator'''

    @staticmethod
    def get_random_serial_number():
        '''Generate a random serial number'''

        minimum_number_part = 1000
        maximum_number_part = 9999

        return str(random.randint(minimum_number_part, maximum_number_part)) + '-' + str(random.randint(minimum_number_part, maximum_number_part))
