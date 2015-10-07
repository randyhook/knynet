class Sensor:
    '''Base class for sensors'''

    def __init__(self, name):
        self.name = name

    def power_up(self):
        '''Power up the sensor'''
