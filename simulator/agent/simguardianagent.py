from simulator.agent.simagent import SimAgent
from agent.guardianagent import GuardianAgent

from simulator.agent.agencies.simaudioagency import SimAudioAgency
from simulator.agent.agencies.simnaturallanguageagency import SimNaturalLanguageAgency

from simulator.bots.sensors.simaudio import SimAudio

class SimGuardianAgent(SimAgent, GuardianAgent):
    '''A Guardian Agent for use with the Simulator'''

    def set_agencies(self):
        self.agencies['audio'] = SimAudioAgency(self)
        self.agencies['natural_language'] = SimNaturalLanguageAgency(self)

    def set_sensors(self):
        self.sensors['audio'] = SimAudio('main_audio')
