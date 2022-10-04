from sqlite3 import OperationalError
import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event): # 練習3
    btn =event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END,num) # 練習5

def click_equal(event): # 練習7
    eqn = entry.get()
    ans = eval(eqn)
    entry.delete(0,tk.END)
    entry.insert(tk.END,ans)

def click_AC(event):
    entry.delete(0,tk.END)

def mouse_over(event):
    event.widget["bg"] = "#CCFFFF"

def mouse_leave(event):
    event.widget["bg"] = "SystemButtonFace"

root = tk.Tk() # 練習1
root.geometry("370x610")

entry = tk.Entry(root,width=10,font=(", 40"),justify="right") # 練習4
entry.grid(row=0,column=0,columnspan=4)

r, c = 1, 0

numbers = list(range(9,-1,-1))
operators = ["/","*","-","+"]

for i, num in enumerate(numbers, 1): # numbersの実装
    btn = tk.Button(root,text=f"{num}", font=("",30),width=4,height=2)
    btn.bind("<1>", click_number)
    btn.grid(row=r,column=c)

    btn.bind("<Enter>",mouse_over)
    btn.bind("<Leave>",mouse_leave)

    c += 1
    if i%3 == 0:
        r += 1
        c = 0

for j, ope in enumerate(operators, 1): # operatorsの実装
    btn = tk.Button(root,text=f"{ope}", font=("",30),width=4,height=2)
    btn.bind("<1>", click_number)
    btn.grid(row=j,column=3)
    btn.bind("<Enter>",mouse_over)
    btn.bind("<Leave>",mouse_leave)

btn = tk.Button(root,text="=", font=("",30),width=4,height=2) # =の実装
btn.bind("<1>", click_equal)
btn.grid(row=r,column=c)
btn.bind("<Enter>",mouse_over)
btn.bind("<Leave>",mouse_leave)

btn = tk.Button(root,text=".", font=("",30),width=4,height=2) # .の実装
btn.bind("<1>", click_number)
btn.grid(row=r,column=c+1)
btn.bind("<Enter>",mouse_over)
btn.bind("<Leave>",mouse_leave)

btn = tk.Button(root,text="AC", font=("",30),width=17,height=2) # ACの実装
btn.bind("<1>", click_AC)
btn.grid(row=5,column=0,columnspan=4)
btn.bind("<Enter>",mouse_over)
btn.bind("<Leave>",mouse_leave)

root.mainloop()