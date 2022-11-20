from frame_main import *


win_options = Frame(win,background=COLOR1,width=WIDTH,height=HEIGHT)

def return_home():
    SCREEN.set('HOME')

def on_enter_up(e):
    e.widget['background'] = COLOR6
    win.bind('<Key>', key_press_up)

def on_enter_down(e):
    e.widget['background'] = COLOR6
    win.bind('<Key>', key_press_down)
    
def on_enter_right(e):
    e.widget['background'] = COLOR6
    win.bind('<Key>', key_press_right)

def on_enter_left(e):
    e.widget['background'] = COLOR6
    win.bind('<Key>', key_press_left)

def on_enter_pause(e):
    e.widget['background'] = COLOR6
    win.bind('<Key>', key_press_pause)

def on_enter_boss(e):
    e.widget['background'] = COLOR6
    win.bind('<Key>', key_press_boss)

def on_enter_home(e):
    e.widget['background'] = COLOR3

def on_leave(e):
    e.widget['background'] = COLOR4
    win.unbind('<Key>')

def on_leave_home(e):
    e.widget['background'] = COLOR2

def key_press_up(e):
    UP.set(e.keysym)

def key_press_down(e):
    DOWN.set(e.keysym)

def key_press_right(e):
    RIGHT.set(e.keysym)

def key_press_left(e):
    LEFT.set(e.keysym)

def key_press_pause(e):
    PAUSE.set(e.keysym)

def key_press_boss(e):
    BOSS.set(e.keysym)

def display_options(win_options):
    X=70
    Y=260
    D=300

    Label(win_options,text="Up:", font=(FONT1, 18), width=10, height=2, bg=COLOR6, relief='raised', fg=COLOR5).place(x=X, y=Y)
    Label(win_options,text="Down:", font=(FONT1, 18), width=10, height=2, bg=COLOR6, relief='raised', fg=COLOR5).place(x=X+D, y=Y)
    Label(win_options,text="Right:", font=(FONT1, 18), width=10, height=2, bg=COLOR6, relief='raised', fg=COLOR5).place(x=X, y=Y+100)
    Label(win_options,text="Left:", font=(FONT1, 18), width=10, height=2, bg=COLOR6, relief='raised', fg=COLOR5).place(x=X+D, y=Y+100)
    Label(win_options,text="Pause:", font=(FONT1, 18), width=10, height=2, bg=COLOR6, relief='raised', fg=COLOR5).place(x=X, y=Y+200)
    Label(win_options,text="Boss Key:", font=(FONT1, 18), width=10, height=2, bg=COLOR6, relief='raised', fg=COLOR5).place(x=X+D, y=Y+200)


    label_up=Label(win_options, textvariable=UP, width=5, height=2, bg=COLOR4, fg=COLOR5, relief='raised', font=("Comic Sans MS", 18))
    label_down=Label(win_options, textvariable=DOWN, width=5, height=2, bg=COLOR4, fg=COLOR5, relief='raised', font=("Comic Sans MS", 18))
    label_right=Label(win_options, textvariable=RIGHT, width=5, height=2, bg=COLOR4, fg=COLOR5, relief='raised', font=("Comic Sans MS", 18))
    label_left=Label(win_options, textvariable=LEFT, width=5, height=2, bg=COLOR4, fg=COLOR5, relief='raised', font=("Comic Sans MS", 18))
    label_pause=Label(win_options, textvariable=PAUSE, width=5, height=2, bg=COLOR4, fg=COLOR5, relief='raised', font=("Comic Sans MS", 18))
    label_boss=Label(win_options, textvariable=BOSS, width=5, height=2, bg=COLOR4, fg=COLOR5, relief='raised', font=("Comic Sans MS", 18))

    X=230
    label_up.place(x=X, y=Y)
    label_down.place(x=X+D, y=Y)
    label_right.place(x=X, y=Y+100)
    label_left.place(x=X+D, y=Y+100)
    label_pause.place(x=X, y=Y+200)
    label_boss.place(x=X+D, y=Y+200)

    button_home=Button(win_options, text='BACK', font=(FONT1, 8), width=10, height=2, command=return_home, bg=COLOR2)
    button_home.place(x=5, y=5)    

    Canvas(win_options, width=700, height=10, bg=COLOR4, bd=0, highlightthickness=1,highlightbackground='black').place(x=0, y=200)

    Label(win_options, text="CONTROLS", font=("Comic Sans MS", 28),bg=COLOR1).place(x=240,y=125)

    label_up.bind('<Enter>', on_enter_up)
    label_up.bind('<Leave>', on_leave)
    label_down.bind('<Enter>', on_enter_down)
    label_down.bind('<Leave>', on_leave)
    label_right.bind('<Enter>', on_enter_right)
    label_right.bind('<Leave>', on_leave)
    label_left.bind('<Enter>', on_enter_left)
    label_left.bind('<Leave>', on_leave)
    label_pause.bind('<Enter>', on_enter_pause)
    label_pause.bind('<Leave>', on_leave)
    label_boss.bind('<Enter>', on_enter_boss)
    label_boss.bind('<Leave>', on_leave)
    button_home.bind('<Enter>', on_enter_home)
    button_home.bind('<Leave>', on_leave_home)

 