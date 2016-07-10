from humans.human import Human

class SimHuman(Human):
    '''Base Human class'''

    def create(serial_number, first_name, last_name):
        '''Initialize a Human'''

        new_human = Human(serial_number, first_name, last_name)
        return new_human
