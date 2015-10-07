from humans.human import Human

class SimHuman(Human):
    '''Base Human class'''

    def __init__(self, serial_number, first_name, last_name):
        '''Initialize a Human'''
        Human.__init__(self, serial_number, first_name, last_name)

        self.location = None

    def speak(self, msg):
        '''Speak a message'''
