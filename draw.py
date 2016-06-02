from variables import *
import turtle
from tkinter import *
from ERROR import *
from guess import *
from random import choice

##Defined Variables##
GUESS_WORD = choice(pic_list)

def draw():
    
    #Defined Functions#
    def go(x,y):
        T.penup()
        T.goto(x,y)
        T.pendown()
        T.ondrag(T.goto)
        
    def DONE():
        WIN2.destroy()
        T.hideturtle()
        guess(GUESS_WORD,WIN)
        #try:
        #    guess(GUESS_WORD,WIN)
        #except:
        #    print(GUESS_ERROR)
    
    def win_2_setup(WIN):
        global L1,B1
        L1 = Label(WIN,text="The picture to draw is a: "+GUESS_WORD)
        L1.pack()
        B1 = Button(WIN,text="Done",command=DONE)
        B1.pack(side=BOTTOM)
        
    #Turtle Window Setup#
    WIN = turtle.Screen()
    WIN.setup(1440,900)
    WIN.title("Guess the Pic: Turtle")
    WIN.bgpic("Pictures/Turtle_BG.gif")
    
    #Tkinter Window Setup#
    WIN2 = Tk()
    WIN2.geometry("225x225")
    WIN2.resizable(False,False)
    WIN2.title("Guess the Pic: Draw")
    try:
        win_2_setup(WIN2)
    except:
        print(WIN_ERROR)
        pass
    
    #Turtle Setup#
    global T
    T = turtle.Turtle()
    T.speed(0)
    T.shapesize(0.5,0.5)
    T.shape("circle")
    
    ##Main##
    WIN.onscreenclick(go)
    
    #Mainloops#
    WIN.mainloop()
    WIN2.mainloop()