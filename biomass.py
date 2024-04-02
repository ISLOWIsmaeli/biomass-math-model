import tkinter as tk
from tkinter import ttk

window=tk.Tk()
my_label=ttk.Label(window,text="First Tkinter!")
my_label.grid(row=1,column=1)
window.mainloop()