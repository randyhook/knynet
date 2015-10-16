from bots.bot import Bot
from simulator.bots.brain.simbrain import SimBrain
from simulator.events.audioevent import AudioEvent

class SimBot(Bot):
    '''A Bot to be used in a simulated environment'''

    def __init__(self, serial_number, name, owner, subowners = None, chain_of_command = None):
        '''Initialize a SimBot'''

        Bot.__init__(self, serial_number, name, owner, subowners, chain_of_command)

        self.brain = SimBrain(serial_number, name, owner, subowners, chain_of_command)

        self.sensory_data_queue = list()

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

    def queue_sensory_data(self, sd):
        '''Queue sensory data to handle later'''

        self.sensory_data_queue.append(sd)

    def update(self, sim_time):
        '''Main update loop for bot'''
        
        messages = list();

        # check sensory data queue
        for s in self.sensory_data_queue:
            # since this is a simulation, we don't even know if we can handle the sensory data that as passed to us from Simulator,
            # so we need to check if we have the right sensor that would have picked it up
            if (s.data_type == 'audio'):
                if 'audio' in self.sensors:
                    self.brain.queue_sensory_data(s)

        self.sensory_data_queue.clear()

        for m in self.brain.process_sensory_data_queue():
            messages.append(m)

        return messages
