import tkinter as tk

window = tk.Tk()
window.title("Menu Example")
window.geometry("280x50")

lab = tk.Label(window, text ='Menu', font = "50")

lab.pack()

menubutton = tk.Menubutton(window, text="Gruppe 1")

menubutton.menu = tk.Menu(menubutton)
menubutton["menu"] = menubutton.menu

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

menubutton.menu.add_checkbutton(label="Fabi",
                                variable=var1)
menubutton.menu.add_checkbutton(label="Miri",
                                variable=var2)
menubutton.menu.add_checkbutton(label="Viv",
                                variable=var3)

menubutton.pack()
window.mainloop()
