from bots.sensors.sensor import Sensor

class AudioSensor(Sensor):
    '''Base class for an Audio Sensor'''

    # This is software that will be embedded on a real world sensor

    def power_up(self):
        '''Power up the sensor'''

    def process_audio(self):
        pass
