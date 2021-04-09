from tkinter import *

class Build:

    def __init__(self, title, size):
        self.root = Tk()
        self.title = title
        self.geometry = size

    def appbuild(self):
        root = self.root
        root.title(self.title)
        root.geometry(self.geometry)

    def btn(self, text, position_x, position_y, **kwargs):
        btn=Button(self.root, text=text, fg=kwargs)
        btn.place(x=position_x, y=position_y)

    def appbuildend(self):
        self.root.mainloop()


app = Build('hi', "300x200+10+20")
app.appbuild()
app.btn('hello world', 80, 100, color='blue')
app.appbuildend()
