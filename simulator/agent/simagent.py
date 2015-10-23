from agent.agent import Agent

class SimAgent(Agent):
    '''Base Agent class for use in Simulator'''

    def process_sensory_data_queue(self):
        '''Override for Bot.Brain.process_sensory_data_queue() since here we are dealing with SimSensoryData instead of SensoryData'''

        messages = list();

        for s in self.sensory_data_queue:
            if (s.data_type == 'audio'):
                if 'audio' in self.agencies:
                    for m in self.agencies['audio'].process_sensory_data(s):
                        messages.append(m)

        self.sensory_data_queue.clear()

        return messages

    def queue_sensory_data(self, sd):
        '''Override for Agent.queue_sensory_data() since here we are accepting an SimSensoryData instead of actual SensoryData'''

        # since this is a simulation, we don't even know if we can handle the sensory data that as passed to us from Simulator,
        # so we need to check if we have the right sensor that would have picked it up
        if (sd.data_type == 'audio'):
            if 'audio' in self.sensors:
                self.sensory_data_queue.append(sd)

        return []

    def update(self, sim_time):
        '''Main update loop for agent'''
        
        messages = list();

        for m in self.process_sensory_data_queue():
            messages.append(m)

        return messages
