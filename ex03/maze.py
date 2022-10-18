import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm #練習8
import random

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
        random_bird()
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1

    if mx == gx and my == gy:
        tkm.showinfo(root, "goal!!!")
    
    can.coords("bird", cx, cy) 
    root.after(100, main_proc) #練習7


def random_bird(): #ランダムなこうかとんの画像に変える
    global bird
    bird_n = random.randint(0, 9)
    birds = ["fig/0.png","fig/1.png","fig/2.png","fig/3.png","fig/4.png","fig/5.png","fig/6.png","fig/7.png","fig/8.png","fig/9.png"]
    bird = birds[bird_n]
    bird = tk.PhotoImage(file=f"{bird}")
    can.create_image(cx, cy, image=bird, tag="bird")

def set_start(maze):
    global mx, my
    num_path = 0
    for j in range(maze_tate):
            for i in range(maze_yoko):
                if maze[j][i] == 0:
                    num_path += 1

    startPos = random.randint(0,num_path -1)

    count_s = 0
    for j in range(maze_tate):
        for i in range(maze_yoko):
            if maze[j][i] == 0:
                if count_s == startPos:
                    mx, my = (i, j)
                    return mx, my
                else:
                    count_s += 1

def set_goal(maze):
    global gx, gy
    num_path = 0
    for j in range(maze_tate):
            for i in range(maze_yoko):
                if maze[j][i] == 0:
                    num_path += 1

    goalPos = random.randint(0, num_path - 1)

    count_g = 0
    for j in range(maze_tate):
        for i in range(maze_tate):
            if maze[j][i] == 0:
                if count_g == goalPos:
                    gx, gy = (i, j)
                    return gx, gy
                else:
                    count_g += 1


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") # 練習1

    can = tk.Canvas(root, width=1500, height=900, bg="black")
    can.pack() #練習2

    maze_tate = 9
    maze_yoko = 15

    maze_sig = mm.make_maze(maze_yoko, maze_tate) #練習9

    mm.show_maze(can, maze_sig) #練習10

    bird = tk.PhotoImage(file="fig/7.png")

    mx, my = set_start(maze_sig)
    gx, gy = set_goal(maze_sig)

    cx, cy = mx * 100 + 50, my * 100 + 50 #練習11
    can.create_image(cx, cy, image=bird, tag="bird") #練習3

    key = "" #練習4

    root.bind("<KeyPress>", key_down) #練習5

    root.bind("<KeyRelease>", key_up) #練習6

    root.after(10,main_proc) #練習7

    root.mainloop()