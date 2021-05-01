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
import random
from tkinter import *
root = Tk()
root.title("2048")

class gamegrid:
    def __init__(self):
        self.bd = ['']* 16



class Rectangle:
   def __init__(self, length, breadth, unit_cost=0):
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   def get_area(self):
       return self.length * self.breadth
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost
# breadth = 120 units, length = 160 units, 1 sq unit cost = Rs 2000
r = Rectangle(160, 120, 2000)
print("Area of Rectangle: %s sq units" % (r.get_area()))
print("blah %s blah" % 50)

root.mainloop()
# ***********************************************************************************
# root.geometry("500x600")
# score = 0
# leftframe = Frame(root, borderwidth=2, relief='raised')
# rightframe = Frame(root, borderwidth=2, relief='ridge')
# leftframe.pack(side=LEFT)
# rightframe.pack(side=RIGHT)
# # Frame relief types = flat (default), raised, sunken, groove, ridge
# headerlabel = Label(leftframe, text="2048", font=("Arial", 25))
# subheaderlabel = Label(leftframe, text="THE GAME", font=("Arial", 10))
# scorelabel = Label(rightframe, text=("SCORE: " + str(score)), width=15)
# resetbutton = Button(rightframe, text="New Game")
# headerlabel.pack()
# subheaderlabel.pack()
# scorelabel.pack()
# resetbutton.pack()
# pad = 3
# gameframe = Frame(root, borderwidth=2, relief='groove', bg="brown", padx=pad, pady=pad)
# gameframe.pack()

# TODO: Find way to name variables as you run through for loop
# d = {}
# for x in range(4):
#     for y in range(4):
#         # row = 0, column = 0
#         # cell00 = Label(...)
#         [cell + 5] = Label(gameframe, height=5, width=10, text="0", bg="grey")
#         # d["cell" + str(x) + str(y)] = ""
#         # globals()["cell" + str(x) + str(y)] = Label(gameframe, height=5, width=10, text="df", bg="green")\
#         #     .grid(row=x, column=y, padx=pad, pady=pad)
#         # label = Label(gameframe, height=5, width=10, text="0", bg="grey")
#         label.grid(row=x, column=y)

# cell00 = Label(gameframe, height=5, width=10, text="00", bg="grey").grid(row=0, column=0)
# cell01 = Label(gameframe, height=5, width=10, text="01", bg="grey").grid(row=0, column=1)
# cell02 = Label(gameframe, height=5, width=10, text="02", bg="grey").grid(row=0, column=2)
# cell03 = Label(gameframe, height=5, width=10, text="03", bg="grey").grid(row=0, column=3)
# cell10 = Label(gameframe, height=5, width=10, text="10", bg="grey").grid(row=1, column=0)
# cell11 = Label(gameframe, height=5, width=10, text="11", bg="grey").grid(row=1, column=1)
# cell12 = Label(gameframe, height=5, width=10, text="12", bg="grey").grid(row=1, column=2)
# cell13 = Label(gameframe, height=5, width=10, text="13", bg="grey").grid(row=1, column=3)
# cell20 = Label(gameframe, height=5, width=10, text="20", bg="grey").grid(row=2, column=0)
# cell21 = Label(gameframe, height=5, width=10, text="21", bg="grey").grid(row=2, column=1)
# cell22 = Label(gameframe, height=5, width=10, text="22", bg="grey").grid(row=2, column=2)
# cell23 = Label(gameframe, height=5, width=10, text="23", bg="grey").grid(row=2, column=3)
# cell30 = Label(gameframe, height=5, width=10, text="30", bg="grey").grid(row=3, column=0)
# cell31 = Label(gameframe, height=5, width=10, text="31", bg="grey").grid(row=3, column=1)
# cell32 = Label(gameframe, height=5, width=10, text="32", bg="grey").grid(row=3, column=2)
# cell33 = Label(gameframe, height=5, width=10, text="33", bg="grey").grid(row=3, column=3)




# def newgame():
#     print("new game")
#     choices = ["2", "4"]
#     weights = [1000, 350]
#     random1 = random.choices(choices, weights)
#     random2 = random.choices(choices, weights)
#     #print(random1)
#     x1 = str(random.randrange(0, 4, 1))
#     y1 = str(random.randrange(0, 4, 1))
#
#     # x2
#     # y2
#     # print(x1 + ", " + y1 + ", ")
#
# resetbutton.config(command=newgame)
# newgame()




# import tkinter as tk
# class App(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.pack()
#
#         self.entrythingy = tk.Entry()
#         self.entrythingy.pack()
#
#         # Create the application variable.
#         self.contents = tk.StringVar()
#         # Set it to some value.
#         self.contents.set("this is a variable")
#         # Tell the entry widget to watch this variable.
#         self.entrythingy["textvariable"] = self.contents
#
#         # Define a callback for when the user hits return.
#         # It prints the current value of the variable.
#         self.entrythingy.bind('<Key-Return>',
#                              self.print_contents)
#
#     def print_contents(self, event):
#         print("Hi. The current entry content is:",
#               self.contents.get())
#
# root = tk.Tk()
# app = App(root)
# app.mainloop()




