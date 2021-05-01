# Calculator

from tkinter import *


root = Tk()
root.title("Calculator")
#root.iconbitmap('c:/...')

calc_display = Entry(root, width=50)
calc_display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipady=5)

num1 = None
num2 = None
oper = None
formula_operator = False
solution = None


def myClick(number):
    def f():
        global num1
        global num2
        global solution

        if not formula_operator:
            solution = None
            if num1 is None:
                num1 = number
            else:
                num1 += number
        else:
            if num2 is None:
                num2 = number
            else:
                num2 += number
        print("Numbers: " + str(num1) + " " + str(oper) + " " + str(num2) + " " + str(solution))
        calc_display.delete(0, END)
        if num2 is None:
            if oper is None:
                calc_display.insert(0, num1)
            else:
                calc_display.insert(0, num1 + oper)
        else:
            calc_display.insert(0, num1 + oper + num2)
    return f


def myClickMultiply():
    global formula_operator
    global oper
    global num1
    global solution
    if num2 != None:
        myClickSolve()
    if num1 is None:
        num1 = solution
        solution = None

    formula_operator = True
    oper = "x"
    print("Numbers: " + str(num1) + " " + str(oper) + " " + str(num2) + " " + str(solution))
    calc_display.delete(0, END)
    calc_display.insert(0, num1 + oper)


def myClickAdd():
    global formula_operator
    global oper
    global num1
    global solution
    if num2 != None:
        myClickSolve()
    if num1 is None:
        num1 = solution
        solution = None

    formula_operator = True
    oper = "+"
    calc_display.delete(0, END)
    calc_display.insert(0, num1 + oper)


def myClickSubtract():
    global formula_operator
    global oper
    global num1
    global solution
    if num2 != None:
        myClickSolve()
    if num1 is None:
        num1 = solution
        solution = None

    formula_operator = True
    oper = "-"
    calc_display.delete(0, END)
    calc_display.insert(0, num1 + oper)


def myClickDivide():
    global formula_operator
    global oper
    global num1
    global solution
    if num2 != None:
        myClickSolve()
    if num1 is None:
        num1 = solution
        solution = None

    formula_operator = True
    oper = "/"
    calc_display.delete(0, END)
    calc_display.insert(0, num1 + oper)


# TODO: is there a way to chose between int or float depending on outcome?

def myClickSolve():
    global solution
    global formula_operator
    global num1
    global num2
    global oper
    if num1 and num2:
        if oper == "x":
            solution = str(float(num1)*float(num2))
            num1 = None
            num2 = None
            oper = None
            formula_operator = False
        if oper == "+":
            solution = str(float(num1)+float(num2))
            num1 = None
            num2 = None
            oper = None
            formula_operator = False
        if oper == "-":
            solution = str(float(num1)-float(num2))
            num1 = None
            num2 = None
            oper = None
            formula_operator = False
        if oper == "/":
            solution = str(float(num1)/float(num2))
            num1 = None
            num2 = None
            oper = None
            formula_operator = False
        calc_display.delete(0, END)
        calc_display.insert(0, str(solution))
        oper = None


def myClickSign():
    current = calc_display.get()
    global num1
    global num2
    if num2 != None:
        num2 = str(-float(num2))
        calc_display.delete(0, END)
        calc_display.insert(0, num1 + oper + num2)
    elif oper is None:
        num1 = str(-float(num1))
        calc_display.delete(0, END)
        calc_display.insert(0, num1)


def myClickClear():
    global formula_operator
    global oper
    global num1
    global num2
    global solution

    num1 = None
    num2 = None
    oper = None
    solution = None
    formula_operator = False

    calc_display.delete(0, END)


def myClickCE():
    global formula_operator
    global oper
    global num1
    global num2
    global solution

    if num2 != None:
        calc_display.delete(len(calc_display.get())-len(num2), END)
        num2 = None
    elif oper != None:
        pass
    elif num1 != None:
        calc_display.delete(0, END)
        num1 = None


def myClickBS():
    global num1
    global num2
    global oper
    global formula_operator

    if num2 != None:
        size = len(num2)
        num2 = num2[:size - 1]
        calc_display.delete(len(calc_display.get())-1, END)
        if num2 == "":
            num2 = None
    elif oper != None:
        oper = None
        formula_operator = False
        calc_display.delete(len(calc_display.get())-1, END)
    elif num1 != None:
        size = len(num1)
        num1 = num1[:size-1]
        calc_display.delete(len(calc_display.get())-1, END)
        if num1 == "":
            num1 = None


buttons = [
    ["CE", "C", "<--", "/"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="]
]

offset = 1

for row in buttons:
    for column in row:
        r = buttons.index(row)
        c = row.index(column)
        if column == "+/-":
            Button(root, text=column, width=8, height=4, command=myClickSign).grid(row=r+offset, column=c)
        elif column == "=":
            Button(root, text=column, width=8, height=4, command=myClickSolve).grid(row=r+offset, column=c)
        elif column == "x":
            Button(root, text=column, width=8, height=4, command=myClickMultiply).grid(row=r+offset, column=c)
        elif column == "C":
            Button(root, text=column, width=8, height=4, command=myClickClear).grid(row=r + offset, column=c)
        elif column == "CE":
            Button(root, text=column, width=8, height=4, command=myClickCE).grid(row=r + offset, column=c)
        elif column == "<--":
            Button(root, text=column, width=8, height=4, command=myClickBS).grid(row=r+offset, column=c)
        elif column == "-":
            Button(root, text=column, width=8, height=4, command=myClickSubtract).grid(row=r + offset, column=c)
        elif column == "+":
            Button(root, text=column, width=8, height=4, command=myClickAdd).grid(row=r+offset, column=c)
        elif column == "/":
            Button(root, text=column, width=8, height=4, command=myClickDivide).grid(row=r+offset, column=c)
        else:
            Button(root, text=column, width=8, height=4, command=myClick(column)).grid(row=r+offset, column=c)

root.mainloop()
