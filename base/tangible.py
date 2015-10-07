class Tangible:
    '''Base class for physical objects'''

    def __init__(self):
        self.location = None

    def get_location(self):
        return self.location
