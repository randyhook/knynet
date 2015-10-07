import unittest
from simulator.bots.simbot import SimBot
from simulator.simhuman import SimHuman

class TestSimBot(unittest.TestCase):
    '''Unit tests for SimBots'''

    def test_init_name(self):
        '''Verify that an exception is raised if a SimBot is intialized without a name'''

        self.assertRaises(ValueError, SimBot, 'NDR-113', '', SimHuman('Little', 'Miss', '123'))

    def test_init_serial_number(self):
        '''Verify that an exception is raised if a SimBot is intialized without a serial number'''

        self.assertRaises(ValueError, SimBot, '', 'testbot', SimHuman('Little', 'Miss', '123'))

    def test_init_owner(self):
        '''Verify that an exception is raised if a SimBot is intialized without a SimHuman owner'''

        self.assertRaises(TypeError, SimBot, 'NDR-113', 'testbot', 'x')

