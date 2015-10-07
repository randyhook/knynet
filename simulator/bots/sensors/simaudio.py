from simulator.bots.sensors.simsensor import SimSensor

class SimAudio(SimSensor):
    '''Base class for a simulated Audio Sensor'''
    
    def power_down(self):
        '''Power down the sensor'''

        return SimSensor.power_down(self)

    def power_up(self):
        '''Power up the sensor'''

        return SimSensor.power_up(self)


