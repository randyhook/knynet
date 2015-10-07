from bots.sensors.sensor import Sensor

class SimSensor(Sensor):
    '''Base class for simulated sensors'''

    def __init__(self, name, brain):
        # brain arg is so that simulated sensor knows which brain it is connect to; real sensor will be wired to real brain

        self.name = name;
        self.sense_thread = None
        self.brain_connection = brain

    def power_down(self):
        '''Power down the sensor'''

        messages = list();
        messages.append('[sim]' + self.name + ' sensor is offline')

        return messages

    def power_up(self):
        '''Power up the sensor'''

        messages = list()
        messages.append('[sim]' + self.name + ' sensor is online')
        return messages

    def sense(self):
        '''Sense the environment'''

        #print('Sensing environment')
        pass
