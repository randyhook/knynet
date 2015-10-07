class Order:
    '''Base Order class'''

    def __init__(self, command, issued_by):
        '''Initialize an order'''

        self.raw_order = command
        self.issued_by = issued_by
