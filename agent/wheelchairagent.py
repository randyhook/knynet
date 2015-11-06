from agent.agent import Agent
from agent.goal import Goal
from agent.goal import GoalType

from agent.agencies.navigatoragency import NavigatorAgency
from simulator.agent.agencies.simnaturallanguageagency import SimNaturalLanguageAgency
from simulator.agent.agencies.simaudioagency import SimAudioAgency

class WheelchairAgent(Agent):
    '''A Wheelchair Agent'''

    action_verbs = dict({
        'transport': ['take', 'bring']
    })

    def formulate_goal(self, goal_type, encoded):
        '''Override agent.formulate_goal'''

        candidate_goal = Goal(goal_type, encoded)

        if goal_type == GoalType.order:
            # Since this is an order, encoded starts with an addressee. Extract it so we can deal with just the order(s).
            messages = self.agencies['natural_language'].get_messages_from_command(encoded.raw_message)

            for m in messages:
                # Check if the first word is a verb
                if m[0][1] == 'VB':
                    # Check if the verb is one of the action verbs
                    for v in WheelchairAgent.action_verbs:
                        if m[0][0].lower() in WheelchairAgent.action_verbs[v]:
                            candidate_goal.main_action = v

        return candidate_goal
