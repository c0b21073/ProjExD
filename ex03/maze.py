from email.mime import image
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") # 練習1

    can = tk.Canvas(root, width=1500, height=900, bg="black")
    can.pack() #練習2

    bird = tk.PhotoImage(file="fig/7.png")
    cx, cy = 300, 400
    can.create_image(cx, cy, image=bird, tag="bird")

    root.mainloop()