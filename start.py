from tkinter import *
from simulator.Simulator import Simulator

def start_simulation():

    root = Tk()
    sim = Simulator(root)
    root.mainloop()

if __name__ == '__main__':
    start_simulation()

