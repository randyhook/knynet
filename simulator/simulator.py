import random
from base.observer import Observer

from tkinter import *
from tkinter import ttk

from simulator.world import World
from simulator.tobii import Tobii
from simulator.simhuman import SimHuman

from simulator.agent.simguardianagent import SimGuardianAgent
from simulator.agent.simwheelchairagent import SimWheelchairAgent

from simulator.bots.sensors.simsensorydata import SimSensoryData

class Simulator(Frame, Observer):
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

        self.agents = dict({
            'guardian': SimGuardianAgent(
                name = 'Guardian',
                serial_number = self.world.generate_new_serial_number(),
                owner = self.humans['randy'],
                subowners = [],
                chain_of_command = []
            ),
            'wheelchair': SimWheelchairAgent(
                name = 'Chair',
                serial_number = self.world.generate_new_serial_number(),
                owner = self.humans['randy'],
                subowners = [
                    self.humans['kenny']
                ],
                chain_of_command = []
            )
        });

        self.agents['guardian'].set_agencies()
        self.agents['guardian'].set_sensors()

        self.agents['wheelchair'].chain_of_command = [self.agents['guardian']]
        self.agents['wheelchair'].location = self.world.rooms['living_room']
        self.agents['wheelchair'].set_agencies()
        self.agents['wheelchair'].set_sensors()

        self.humans['kenny'].location = self.agents['wheelchair'].location

        self.tobii = Tobii()
        self.tobii.location =  self.agents['wheelchair'].location

        self.scripts = dict()
        self.scripts['wheelchair_to_room'] = dict({
            'time': 1000,
            'sensory_data': SimSensoryData(
                data_type = 'audio',
                data = 'Chair. Take me to my room.',
                origin = self.humans['kenny']
            )
        });

        self.setup_display()

        self.sim_time = 0
        self.update_delta_milliseconds = 100
        self.start_simulation()

    def display_output(self, messages):
        if not isinstance(messages, list):
            message = messages
            messages = list();
            messages.append(message)

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
        for a in self.agents:
            self.agents[a].shut_down()

        #quit()

    def run_scripts(self):
        # check for scripts that are due and run them
        scripts_run = list()
        for s in self.scripts:
            if self.sim_time > self.scripts[s]['time']:
                scripts_run.append(s)

                # send the script to each agent
                #
                # right now we are forcing each agent to handle each script. the agent will determine if it is able to handle the script.
                # we could eventually have the simulator be more realistic by broadcasting events and each agent would have sim sensors
                # monitoring the environment for events it can react to.
                for a in self.agents:
                    self.agents[a].queue_sensory_data(self.scripts[s]['sensory_data'])

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

        # make the simulation an observer of each agent's memory activity
        for a in self.agents:
            self.agents[a].memory.attach_observer(self)

        # start up the bots
        for a in self.agents:
            self.agents[a].start_up()

        self.after(self.update_delta_milliseconds, self.update_sim)
        self.mainloop()

        return

    def update_from_observable(self, notification):
        self.display_output('[' + notification.message_from + '](' + notification.from_function + ') ' + notification.message)

    def update_sim(self):
        # increment the time counter
        self.sim_time = self.sim_time + self.update_delta_milliseconds

        self.run_scripts()

        # tell each agent to update itself
        for a in self.agents:
            self.agents[a].update(self.sim_time)

        # run this function again after time
        self.after(self.update_delta_milliseconds, self.update_sim)

