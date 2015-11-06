from agent.memory import Memory
from agent.goal import Goal
from agent.goal import GoalType

from datetime import datetime

class DecisionEngine():
    '''Base Decision Engine class'''

    def __init__(self, agent):
        self.agent = agent

    def i_am_being_addressed(self, message):
        # get the addressee
        if 'natural_language' in self.agent.agencies:
            addressee = self.agent.agencies['natural_language'].get_addressee(message)
        else:
            return False

        # check if the number of agent name components match the components in the addressee;
        # if not, someone else must be being addressed
        if len(addressee) != len(self.agent.name.split(' ')):
            return False

        # for each word in the agent's name
        name_part_counter = 0
        for name_part in self.agent.name.split(' '):

            # check if name part matches same position in addressee
            if (name_part.lower() != addressee[name_part_counter].lower()):
                return False

            name_part_counter = name_part_counter + 1

        return True

    def prioritize_goals(self):
        pass

    def process_command(self, encoded):
        # check if addresser has the authority to issue command to this agent
        if encoded.spoken_by == self.agent.owner or encoded.spoken_by in self.agent.subowners or encoded.spoken_by in self.agent.chain_of_command:
            candidate_goal = self.agent.formulate_goal(GoalType.order, encoded)

            # check if this command can be carried out

            # check if the command conflicts with any existing internal goals
            conflicted = False
            for g in self.agent.memory.goals:
                # TODO: if conflict, conflicted_goals.append(g)
                pass

            if not conflicted:
                self.agent.memory.store_goal(candidate_goal)
                self.prioritize_goals()
            else:
                # TODO: resolve conflicts
                pass

    def process_language(self, encoded):
        # check if this agent is being addressed
        if (self.i_am_being_addressed(encoded.encoded_message)):
            # check if this is a command
            is_command = False
            if ('natural_language' in self.agent.agencies):
                if self.agent.agencies['natural_language'].is_command(encoded.encoded_message):
                    self.process_command(encoded)

    def process_sensory_encoded(self, encoded):
        # store the data to memory
        self.agent.memory.store_sensory_encoded(encoded) 

        # process the data into knowledge
        if (encoded.data_type == 'language'):
            self.process_language(encoded)
