from tkinter import *
from tkinter import messagebox

calc = Tk()                         # Making the basic window
calc.geometry("312x394+300+100")    # The window's side width: 312, height: 394 & The window's positioning 300 pixels from the right, 100 pixels down
calc.resizable(0, 0)                # This prevents the window from resizing
calc.title("Calculator")            # Name of the window

#needed for declaring Calculator() as an argument
input_text = ""
