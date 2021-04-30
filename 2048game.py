#Requirements (per rosettacode.org/wiki/2048)

# 1. "Non-greedy" movement. The titles that were created by combining other tiles should not be combined again during
# the same turn (move). That is to say that moving the tile row of [2][2][2][2] to the right should result
# in ......[4][4] and not .........[8]
# 2. "Move direction priority". If more than one variant of combining is possible, move direction shall indicate which
# combination will take effect. For example, moving the tile row of ...[2][2][2] to the right should result in
# ......[2][4] and not ......[4][2]
# 3. Adding a new tile on a blank space. Most of the time, a new "2" is to be added and occasionally (10% of the time)
# - a "4".
# 4. Check for valid moves. The player shouldn't be able to skip their turn by trying a move that doesn't change the
# board.
# 5. Win condition.
# 6. Lose condition.


# game grid is 4x4
# score is increased by result of any combinations
# controls: choose direction, all tiles shift in that direction. if two numbers are the same, they combine
# cannot choose the same direction twice in a row

#from tkinter import *

#root = Tk()
#root.title = 2048
import tkinter as tk
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-leftarrow>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
app = App(root)
app.mainloop()




