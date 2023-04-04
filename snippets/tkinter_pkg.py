#

import tkinter.messagebox
tkinter.messagebox.showinfo('Hello Workd')

# but not messagebox.showinfo('H-W') if you only import
# tkinter.messagebox as is
tkinter.messagebox.showinfo("but not messagebox.showinfo('H-W') if you"
                            " only import tkinter.messagebox as is")
#NameError: name 'messagebox' is not defined

import tkinter.messagebox as messagebox
messagebox.showinfo('Hello Workd .__again()')

# or
from tkinter.messagebox import showinfo
showinfo('Third > Hello Workd')
