# -*- coding:utf-8 -*-
# Date: 2020/3/13

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk
    
    
root = tk.Tk()
root.geometry("200x300+500+600")

hscrollbar = tk.Scrollbar(root)
hscrollbar.pack(side=tk.RIGHT, fill="y")

test_text = tk.Text(root, wrap=tk.NONE, yscrollcommand=hscrollbar.set)
test_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
poem_name = "Do Not Go Gentle into That Good Night.txt"
msg = "This is tkinter or Tkinter!\n"*50
test_text.insert(tk.END, msg)

hscrollbar.config(command=test_text.xview)

root.mainloop()