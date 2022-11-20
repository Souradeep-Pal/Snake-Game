from tkinter import *
#from playsound import playsound
WIDTH = 700
HEIGHT = 600
APP_NAME = "Snake Game"
DIM = str(WIDTH) + str('x') + str(HEIGHT)

win = Tk()
win.title(APP_NAME)
win.resizable(False, False)
win.geometry(DIM)

win.config(cursor="left_ptr")

#playsound("home_adventure.mp3",False)

COLOR1='#98b503'
COLOR2='yellow green'
COLOR3='lawn green'
COLOR4='darkorange4'
COLOR5='white'
COLOR6='darkorange3'

FONT1="Comic Sans MS"

SCREEN = StringVar(win, 'HOME')

UP=StringVar(win,'Up')
DOWN=StringVar(win,'Down')
RIGHT=StringVar(win,'Right')
LEFT=StringVar(win,'Left')
PAUSE=StringVar(win,'Escape')
BOSS=StringVar(win,'b')
