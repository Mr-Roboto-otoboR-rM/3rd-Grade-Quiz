import tkinter as tk
from tkinter import*
from tkinter import ttk
from math import *
from random import *

LARGE_FONT= ("Verdana", 14)
MED_FONT= ("Verdana", 12)

class QuestionApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

     
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight=2)
        container.grid_columnconfigure(0, weight=2)

        self.frames = {}

        for F in (QuestionPage, WordProblems, Multiply, VolumeMass, Area, Shapes, Unknown, Graphs, Parimeter, ShapesFractions, Time, Ruler, Fractions, Rounding):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(QuestionPage)
    
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class QuestionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="3RD GRADE GOALS: \n        MATH", font = LARGE_FONT)
        label.grid(row=0, column=2)
     
        button = ttk.Button(self, text="Word Problems",
                           command=lambda: controller.show_frame(WordProblems))
        button.grid(row=1, column=0)

        button1 = ttk.Button(self, text="Volume + Mass",
                           command=lambda: controller.show_frame(VolumeMass))
        button1.grid(row=1, column=1)

        button2 = ttk.Button(self, text=" Area ",
                           command=lambda: controller.show_frame(Area))
        button2.grid(row=1, column=3)

        button3 = ttk.Button(self, text="Shapes",
                           command=lambda: controller.show_frame(Shapes))
        button3.grid(row=1, column=4)

        button4 = ttk.Button(self, text="Unknown",
                           command=lambda: controller.show_frame(Unknown))
        button4.grid(row=2, column=0)

        button5 = ttk.Button(self, text="Graphs",
                           command=lambda: controller.show_frame(Graphs))
        button5.grid(row=2, column=1)

        button6 = ttk.Button(self, text="Parimeter",
                           command=lambda: controller.show_frame(Parimeter))
        button6.grid(row=2, column=3)

        button7 = ttk.Button(self, text="Shapes + Fractions",
                           command=lambda: controller.show_frame(ShapesFractions))
        button7.grid(row=2, column=4)

        button8 = ttk.Button(self, text=" Time ",
                           command=lambda: controller.show_frame(Time))
        button8.grid(row=3, column=0)

        button9 = ttk.Button(self, text=" Ruler ",
                           command=lambda: controller.show_frame(Ruler))
        button9.grid(row=3, column=1)

        button10 = ttk.Button(self, text="Fractions",
                           command=lambda: controller.show_frame(Fractions))
        button10.grid(row=3, column=3)

        button11 = ttk.Button(self, text="Rounding",
                           command=lambda: controller.show_frame(Rounding))
        button11.grid(row=3, column=4)

        button12 = ttk.Button(self, text=" Multiply ",
                           command=lambda: controller.show_frame(Multiply))
        button12.grid(row=1, column=3)

class WordProblems(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Word Problems", font=LARGE_FONT)
        label = tk.Label(self, text="Word Problems", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
      
        e = Entry(self)
        e.pack()

        e.delete(0, END)
        e.insert(0, "Answer Here")

        button = ttk.Button(self, text="Submit",
                            command=lambda: controller.show_frame(QuestionPage))
        button.pack()

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()

class Math(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Math", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()


class GenMultiply(object):

        x = randint(1,10)
        y = randint(1,10)
        ans = x*y

class Multiply(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        mult = GenMultiply()
        a = mult.x
        b = mult.y
        answ = mult.ans

        What_is = "What is %s x %s?" % (a,b)

        label = ttk.Label(self, text="Multiply", font=LARGE_FONT)        
        label.pack(pady=10, padx=10)

        label2 = ttk.Label(self, text=What_is, font=MED_FONT)
        label2.pack(pady=10, padx=10)

        e = Entry(self)
        e.pack()

        e.delete(0, END)
        e.insert(0, "")

        def convert():
            conv = int(e.get())

        def check():
            print(convert())
            print(answ)
              
        button2 = ttk.Button(self, text="Submit",
                            command=check)
        button2.pack()
        
##        if e.get() == answ:
##            label3 = ttk.Label(self, text="Correct", font=MED_FONT)
##            label3.pack(pady=10, padx=10)
##        else:
##            label3 = ttk.Label(self, text="Incorrect", font=MED_FONT)
##            label3.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()

        
    
class VolumeMass(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Volume + Mass", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()

class Area(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="  Area  ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()

class Shapes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="   Shapes   ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()

class Unknown(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="   Unknown   ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()

class Graphs(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="   Graphs   ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()

class Parimeter(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="   Parimeter   ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()

class ShapesFractions(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Shapes + Fractions  ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()

class Time(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="   Time   ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()

class Ruler(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="   Ruler   ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()

class Fractions(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="   Fractions   ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()

class Rounding(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="   Rounding   ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Quit",
                            command=lambda: controller.show_frame(QuestionPage))
        button1.pack()
        

app = QuestionApp()
app.mainloop()
