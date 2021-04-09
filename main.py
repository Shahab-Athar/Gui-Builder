from tkinter import *

class Build:

    btn_placed = 0

    def __init__(self, title, size):
        self.root = Tk()
        self.title = title
        self.geometry = size

    def create(self):
        root = self.root
        root.title(self.title)
        root.geometry(self.geometry)

    def label(self, position_x, position_y, **kwargs):
        text = kwargs.get('text', '')
        color = kwargs.get('color', 'black')
        size = kwargs.get('size', '10')
        textcolor = kwargs.get('text_color', 'black')
        font = kwargs.get('font', 'Calibri')

        label = Label(self.root, text = text, bd = size, fg = textcolor, font = font)
        label.place(x=position_x, y=position_y)

    def btn(self, position_x, position_y, **kwargs):
        text = kwargs.get('text', '')
        color = kwargs.get('color', 'black')

        command = kwargs.get('command', 'None')

        btn=Button(self.root, text=text, fg=color, command=command)
        btn.place(x=position_x, y=position_y)

        self.btn_placed += 1

    def show(self):
        self.root.mainloop()

    def get_status(self):
        print("\nYour App Is Running.\n\nStatus:      Running\nLogs:")
        print("Buttons: ", self.btn_placed)
