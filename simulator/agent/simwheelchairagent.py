from simulator.agent.simagent import SimAgent
from agent.wheelchairagent import WheelchairAgent

from simulator.agent.agencies.simaudioagency import SimAudioAgency
from simulator.agent.agencies.simnaturallanguageagency import SimNaturalLanguageAgency
from agent.agencies.navigatoragency import NavigatorAgency

from simulator.bots.sensors.simaudio import SimAudio

class SimWheelchairAgent(SimAgent, WheelchairAgent):
    '''A Wheelchair Agent for use with the Simulator'''

    def set_agencies(self):
        self.agencies['audio'] = SimAudioAgency(self)
        self.agencies['natural_language'] = SimNaturalLanguageAgency(self)
        self.agencies['navigator'] = NavigatorAgency()

    def set_sensors(self):
        self.sensors['audio'] = SimAudio('main_audio')
