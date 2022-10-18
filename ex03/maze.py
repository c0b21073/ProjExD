from email.mime import image
import tkinter as tk

def key_down(event):
    global key
    key = event.keysym #練習5


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
    

    root.mainloop()