class Agent():
    '''Base Agent class'''

    def __init__(self, serial_number, name, owner, subowners, chain_of_command):
        self.serial_number = serial_number
        self.name = name
        self.owner = owner
        self.subowners = subowners
        self.chain_of_command = chain_of_command

        self.sensors = dict()
        self.sensory_data_queue = list()

        self.agencies = dict()
        self.standing_orders = list()

    def process_sensory_data_queue(self):
        pass
