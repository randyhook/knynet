from agent.memory import Memory
from agent.decisionengine import DecisionEngine
from agent.goal import Goal
from agent.goal import GoalType

class Agent():
    '''Base Agent class'''

    def __init__(self, serial_number, name, owner, subowners, chain_of_command):
        self.serial_number = serial_number
        self.name = name
        self.owner = owner
        self.subowners = subowners
        self.chain_of_command = chain_of_command

        self.sensors = dict()
        self.sensory_data_queue = list()

        self.memory = Memory(self)
        self.decision_engine = DecisionEngine(self)

        self.agencies = dict()
        self.standing_orders = list()

    def formulate_goal(self, goal_type, encoded):
        return Goal(GoalType.order, encoded)

    def process_sensory_data_queue(self):
        pass
