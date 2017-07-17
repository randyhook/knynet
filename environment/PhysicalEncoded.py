from environment.SensoryEncoded import SensoryEncoded

class PhysicalEncoded(SensoryEncoded):

    def __init__(self, units, value):
        self.units = units
        self.value = value
