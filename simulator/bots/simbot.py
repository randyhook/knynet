from bots.bot import Bot
from simulator.bots.brain.simbrain import SimBrain
from simulator.events.audioevent import AudioEvent

class SimBot(Bot):
    '''A Bot to be used in a simulated environment'''

    def __init__(self, serial_number, name, owner, subowners = None, chain_of_command = None):
        '''Initialize a SimBot'''

        Bot.__init__(self, serial_number, name, owner, subowners, chain_of_command)

        self.brain = SimBrain(serial_number, name, owner, subowners, chain_of_command)
        self.event_queue = list()

    def power_down(self):
        '''Power down the bot'''

        messages = list();
        messages.append('[sim]' + self.brain.name + ' powering down.')

        for s in iter(self.sensors):
            for m in self.sensors[s].power_down():
                messages.append(m)

        messages.append('[sim]' + self.brain.name + ' powered down.')
        
        return messages

    def power_up(self):
        '''Power up the bot'''

        messages = list()
        messages.append('[sim]My name is ' + self.brain.name + ' and my serial number is ' + self.brain.serial_number)

        for s in iter(self.sensors):
            for m in self.sensors[s].power_up():
                messages.append(m)

        return messages

    def queue_event(self, ev):
        '''Queue an event to handle later'''

        self.event_queue.append(ev)

    def update(self, sim_time):
        '''Main update loop for bot'''
        
        messages = list();

        # check event queue
        for e in self.event_queue:
            if (isinstance(e, AudioEvent)):
                if 'audio' in self.sensors:
                    for m in self.brain.queue_sensory_input(e):
                        messages.append(m)

        self.event_queue.clear()

        return messages
