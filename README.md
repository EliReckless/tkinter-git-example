# Tkinter Examples and Screenshots

## Tkinter Button

### Source code example

```python
import tkinter as tk

window = tk.Tk()
window.title("Button Example")
window.geometry("280x50")

btn = tk.Button(window, text="A button", fg="red", bg="yellow")
btn.pack()

window.mainloop()

```

### Screenshot
![Tkinter Button Example](tkinter_button.png "Tkinter Button Example")


## Tkinter Menu and Menubutton

### Source code example

### Screenshot


## Tkinter Scale

### Source code example

### Screenshot


## Tkinter OptionMenu

### Source code example

### Screenshot


## Tkinter Dialogs

### Sourcecode Example

### Screenshot


## Tkinter Checkbutton

### Sourcecode Example

### Screenshot


## Tkinter LabelFrame and RadioButton

### Source code example

### Screenshot


## Tkinter PanedWindow

### Source code example

### Screenshot


## Tkinter Canvas

### Source code example

### Screenshot


## Tkinter Listbox and Scrollbar

```
import tkinter as tk

window = tk.Tk()
window.title("Listbox & Scrollbar example")
window.geometry("280x50")

lb = tk.Listbox(window)
lb.insert(1, "Python")
lb.insert(2, "Perl")
lb.insert(3, "C")
lb.insert(4, "PHP")
lb.insert(5, "JSP")
lb.insert(6, "Ruby")
lb.pack(side = tk.LEFT, fill=tk.BOTH)

sb = tk.Scrollbar(window)
sb.pack(side=tk.RIGHT, fill=tk.BOTH)

lb.config(yscrollcommand = sb.set)
sb.config(command = lb.yview)

window.mainloop()
```

### Screenshot


# Exercise
 - Install git on your machine
 - Create a fork of this repository inside github
 - Clone your fork locally (`git clone`)
 - Add a **source code example** and a **screenshot** to one of the topics inside the `README.md` file
 - Commit your changes and add a meaningful commit message (`git commit`)
 - Push your changes to your fork (`git push`)
 - Create a pull request for your changes inside github
 
## Help
 - [Git Download](https://git-scm.com/downloads)
 - [Project forking workflow](https://guides.github.com/activities/forking/)

