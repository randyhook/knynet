import os
import sys

# setup search paths
basedir = os.path.dirname(__file__)
sys.path.append(basedir + '\\bots\\brain\\agencies\\nltk');

from simulator.simulator import Simulator

def start_simulation():
    '''Start the simulation'''

    sim = Simulator()
    sim.master.title('knynet')

if __name__ == '__main__':
    start_simulation()
