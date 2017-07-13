from tkinter import *

from simulator.SimHuman import SimHuman
from simulator.SimBot import SimBot

from simulator.sensors.SimAudioSensor import SimAudioSensor
from simulator.sensors.SimWeightSensor import SimWeightSensor

from agency.AudioAgency import AudioAgency
from agency.LanguageAgency import LanguageAgency
from agency.PhysicalAgency import PhysicalAgency

class Simulator(Frame):

    stepInterval = 500

    def __init__(self, master=None):

        # instance variables
        self.humans = {}
        self.bots = {}
        self.audioQueue = []

        # set up the frame
        Frame.__init__(self, master)
        self.master = master
        self.initWindow()

        # initialize the sim world
        self.addStatusMessage('Simulator initializing...')

        self.initHumans()
        self.initBots()

        self.addStatusMessage('Simulator initialization complete.')

        # start the timer
        self.after(Simulator.stepInterval, self.nextStep)

    def addStatusMessage(self, msg):

        self.statusArea.insert(END, '\n' + msg)

    def getEnvAudio(self):

        return self.audioQueue

    def humanSpeak(self, speaker):

        self.audioQueue.append(self.parameterEntry.get())
        self.addStatusMessage(speaker + ' spoke: ' + self.parameterEntry.get())

    def initBots(self):

        self.addStatusMessage('Initializing bots.')

        # create the chairbot
        chairbot = SimBot(self, 'Chairbot', self.humans['Randy'])
        chairbot.addSensor(SimAudioSensor(chairbot))
        chairbot.addSensor(SimWeightSensor(chairbot))
        chairbot.agent.addAgency(AudioAgency())
        chairbot.agent.addAgency(LanguageAgency())
        chairbot.agent.addAgency(PhysicalAgency())
        self.bots['ChairBot'] = chairbot

    def initHumans(self):
        
        self.addStatusMessage('Initializing humans.')

        self.humans['Randy'] = SimHuman('Randy')
        talkButtonRandy = Button(self.master, text='Randy-Speak', command=lambda: self.humanSpeak('Randy'))
        talkButtonRandy.grid(row=2, column=1)

    def initWindow(self):

        self.master.title('KNYNET Simulator')

        self.actionLabel = Label(self.master, text='Action parameter')
        self.actionLabel.grid(row=0, columnspan=2)

        # user entry
        self.parameterEntry = Entry(self.master, width=100)
        self.parameterEntry.grid(row=1, columnspan=2)

        stimulateChairBotButton = Button(self.master, text='Stimulate-ChairBot', command=lambda: self.stimulateBot('ChairBot'))
        stimulateChairBotButton.grid(row=2, column=0)
        
        # output
        self.statusArea = Text(self.master, bg='#000000', fg='#ffffff')
        self.statusArea.grid(row=3, columnspan=2)

    def nextStep(self):

        for botKey in list(self.bots.keys()):
            self.bots[botKey].updateFromEnvironment()

        self.audioQueue.clear()

        self.after(Simulator.stepInterval, self.nextStep)

    def stimulateBot(self, bot):

        self.bots[bot].receiveStimuli(self.parameterEntry.get())
