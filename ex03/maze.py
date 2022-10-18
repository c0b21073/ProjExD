import tkinter as tk
import maze_maker as mm #練習8

def key_down(event):
    global key
    key = event.keysym #練習5

def key_up(event):
    global key
    key = "" #練習6

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    
    can.coords("bird", cx, cy) 
    root.after(10, main_proc) #練習7


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") # 練習1

    can = tk.Canvas(root, width=1500, height=900, bg="black")
    can.pack() #練習2

    bird = tk.PhotoImage(file="fig/7.png")
    cx, cy = 300, 400
    can.create_image(cx, cy, image=bird, tag="bird") #練習3

    key = "" #練習4

    root.bind("<KeyPress>", key_down) #練習5

    root.bind("<KeyRelease>", key_up) #練習6

    root.after(100, main_proc) #練習7

    maze_sig = mm.make_maze(15, 9) #練習9

    mm.show_maze(can, maze_sig) #練習10

    root.mainloop()