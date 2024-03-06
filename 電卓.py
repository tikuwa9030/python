import tkinter as tk

labels = ("7","8","9","*","4","5","6","-","1","2","3","+","C","0",".","=")

def clicked(e):
    btn = e.widget["text"]
    if btn == "C":
        entry.delete(0,tk.END)
    elif btn == "=":
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,result)
    else:
        entry.insert(tk.END,btn)

root = tk.Tk()
root.title("電卓")

upper = tk.Frame(root)
entry = tk.Entry(upper,font = ("",25),justify = tk.RIGHT)
entry.pack(fill = tk.X)
upper.pack(padx = 20,pady = 20)

lower = tk.Frame(root)
lower.pack(pady = 20)
for i, txt in enumerate(labels):
    b = tk.Button(lower,width = 4,height = 2,font = ("",25),text = txt)
    b.grid(row = int(i/4),column = i%4)
    b.bind("<Button-1>",clicked)


root.mainloop()

