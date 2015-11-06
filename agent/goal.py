from enum import Enum

class GoalType(Enum):
    order = 0
    inherent = 1

class Goal():
    '''Base Goal class'''

    def __init__(self, goal_type, spoken_language):
        self.goal_type = goal_type
        self.encoded_message = spoken_language.encoded_message
        self.raw_message = spoken_language.raw_message

        self.main_action = ''
