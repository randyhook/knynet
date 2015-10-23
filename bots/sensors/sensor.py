class Sensor:
    '''Base class for sensors'''

    # This is software that will be embedded on a real world sensor

    def __init__(self, name):
        self.name = name

    def power_up(self):
        '''Power up the sensor'''
