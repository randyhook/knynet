import random

from tkinter import *
from tkinter import ttk

from simulator.world import World
from simulator.tobii import Tobii
from simulator.simhuman import SimHuman
from simulator.bots.guardianbot import GuardianBot
from simulator.bots.chairbot import ChairBot

from simulator.events.audioevent import AudioEvent

class Simulator(Frame):
    '''Simulator class'''

    def __init__(self):
        '''Initialize the simulator'''

        random.seed()
        
        self.world = World()

        self.humans = dict({
            'randy': SimHuman(
                first_name = 'Randy',
                last_name = 'Hook',
                serial_number = self.world.generate_new_serial_number()
            ),
            'kenny': SimHuman(
                first_name = 'Kenny',
                last_name = 'Hook',
                serial_number = self.world.generate_new_serial_number()
            )
        });

        self.bots = dict({
            'guardianbot': GuardianBot(
                name = 'GuardianBot',
                serial_number = self.world.generate_new_serial_number(),
                owner = self.humans['randy']
            ),
            'chairbot': ChairBot(
                name = 'ChairBot',
                serial_number = self.world.generate_new_serial_number(),
                owner = self.humans['randy'],
                subowners = [
                    self.humans['kenny'].serial_number
                ]
            )
        });

        self.bots['chairbot'].chain_of_command = [self.bots['guardianbot']]
        self.bots['chairbot'].location = self.world.rooms['living_room']
        self.humans['kenny'].location = self.bots['chairbot'].location

        self.tobii = Tobii()
        self.tobii.location =  self.bots['chairbot'].location

        self.scripts = dict()
        self.scripts['chairbot_to_room'] = dict({
            'time': 1000,
            'event': AudioEvent(
                initiator = self.humans['kenny'].serial_number,
                audio_type = 'voice',
                audio_data = 'ChairBot. Take me to my room.'
            )
        });

        self.setup_display()

        self.sim_time = 0
        self.update_delta_milliseconds = 100
        self.start_simulation()

    def display_output(self, messages):
        for m in messages:
            self.text_output.insert(INSERT, "\n" + str(m))

    def process_command(self):
        '''Process a command from the simulator command line'''

        self.text_output.insert(INSERT, "\n[input]" + self.input_main.get())

        i = self.input_main.get()
        if i == 'quit':
            self.quit_simulation()
        elif i == 'audio':
            self.text_output.insert(INSERT, "\n[audio]")

        self.input_main_text.set('')

    def quit_simulation(self):
        # shut down the bots
        for b in iter(self.bots):
            messages = self.bots[b].power_down()
            self.display_output(messages)

        #quit()

    def run_scripts(self):
        # check for scripts that are due and run them
        scripts_run = list()
        for s in self.scripts:
            if self.sim_time > self.scripts[s]['time']:
                scripts_run.append(s)

                # send the script to each bot
                for b in iter(self.bots):
                    self.bots[b].queue_event(self.scripts[s]['event'])

        # remove any scripts that were just run so they don't run again
        for s in scripts_run:
            del self.scripts[s]

    def setup_display(self):
        Frame.__init__(self)
        self.grid()

        self.text_output = Text(self)
        self.output_scrollbar = Scrollbar(self, orient=VERTICAL, command=self.text_output.yview)
        self.text_output.option_add('yscrollcommand', self.output_scrollbar.set)

        self.text_output.grid(row=0, column=0)
        self.output_scrollbar.grid(row=0, column=1, sticky=N+S)

        self.input_main_label = Label(self, text='Command Line')
        self.input_main_label.grid(row=1, column=0)
        self.input_main_text = StringVar()
        self.input_main = Entry(self, textvariable=self.input_main_text)
        self.input_main.grid(row=2, column=0)
        self.send_command = Button(self, text='Send', command=self.process_command)
        self.send_command.grid(row=3, column=0)


    def start_simulation(self):
        '''Start the simulation'''

        # start up the bots
        for b in iter(self.bots):
            messages = self.bots[b].power_up()
            self.display_output(messages)

        self.after(self.update_delta_milliseconds, self.update_sim)
        self.mainloop()

        return

    def update_sim(self):
        # increment the time counter
        self.sim_time = self.sim_time + self.update_delta_milliseconds

        self.run_scripts()

        # tell each bot to update itself
        for b in iter(self.bots):
            messages = self.bots[b].update(self.sim_time)
            self.display_output(messages)

        # run this function again after time
        self.after(self.update_delta_milliseconds, self.update_sim)

