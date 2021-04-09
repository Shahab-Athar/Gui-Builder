from tkinter import *

class Build:

    btn_placed = 0

    def __init__(self, title, size):
        self.root = Tk()
        self.title = title
        self.geometry = size

    def appbuild(self):
        root = self.root
        root.title(self.title)
        root.geometry(self.geometry)

    def btn(self, text, position_x, position_y, **kwargs):
        color = kwargs.get('color')

        btn=Button(self.root, text=text, fg=color)
        btn.place(x=position_x, y=position_y)

        self.btn_placed += 1

    def appbuildend(self):
        self.root.mainloop()

    def get_status(self):
        print("\nYour App Is Running.\n\nStatus:      Running\nLogs:")
        print("Buttons: ", self.btn_placed)
