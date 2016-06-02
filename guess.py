from variables import *
from tkinter import *
from ERROR import *
from draw import *
import time

def guess(GUESS_WORD,T_WIN):
    
    #Defined Functions#
    def G_WIN():
        print("Guesser Wins")
        L = Label(TK_WIN,text="Guesser Wins")
        L.pack(side=TOP)
        time.sleep(5)
        TK_WIN.destroy()
        raise SystemExit(0)
        
    def D_WIN():
        print("Drawer Wins")
        L = Label(TK_WIN,text="Drawer Wins").pack(side=TOP)
        time.sleep(5)
        TK_WIN.destroy()
        raise SystemExit(0)
        
    def check():
        global G_num
        WORD = E1.get()
        if WORD.lower() == GUESS_WORD.lower():
            G_WIN()
        elif G_num == 1:
            D_WIN()
        else:
            G_num -= 1
            L2.configure(text=("Guesses remain: " + str(G_num)))
            pass
    
    def TK_setup(WIN):
        global E1, L2
        L1 = Label(WIN,text="Guess the word: ").pack(side=TOP)
        L2 = Label(WIN,text=("Guesses remain: "+str(G_num)))
        L2.pack(side=TOP)
        E1 = Entry(WIN)
        E1.pack(side=TOP)
        B1 = Button(WIN,text="Guess",command=check).pack(side=TOP)
        
    #Tkinter Window Setup#
    global TK_WIN
    TK_WIN = Tk()
    TK_WIN.geometry("250x250")
    TK_WIN.title("Guess the Pic: Guess")
    TK_WIN.resizable(False,False)
    TK_setup(TK_WIN)
    #try:
    #    TK_setup(TK_WIN)
    #except:
    #    print(WIN_ERROR)
    #    pass
    
    ##Mainloop##
    TK_WIN.mainloop()
