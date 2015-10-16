class SimSensoryData:
    '''Base class for simulated sensory data'''

    def __init__(self, data_type, data):
        self.data_type = data_type
        self.data = data
