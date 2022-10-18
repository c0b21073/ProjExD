import tkinter as tk
import maze_maker as mm #練習8

def key_down(event):
    global key
    key = event.keysym #練習5

def key_up(event):
    global key
    key = "" #練習6

def main_proc():
    global mx, my
    global cx, cy
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1

    if maze_sig[my][mx] == 0:
        cx, cy = mx * 100 + 50, my * 100 + 50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    
    can.coords("bird", cx, cy) 
    root.after(100, main_proc) #練習7


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") # 練習1

    can = tk.Canvas(root, width=1500, height=900, bg="black")
    can.pack() #練習2

    maze_sig = mm.make_maze(15, 9) #練習9

    mm.show_maze(can, maze_sig) #練習10

    bird = tk.PhotoImage(file="fig/7.png")
    mx, my = 1, 1
    cx, cy = mx * 100 + 50, my * 100 + 50 #練習11
    can.create_image(cx, cy, image=bird, tag="bird") #練習3

    key = "" #練習4

    root.bind("<KeyPress>", key_down) #練習5

    root.bind("<KeyRelease>", key_up) #練習6

    root.after(10,main_proc) #練習7

    root.mainloop()