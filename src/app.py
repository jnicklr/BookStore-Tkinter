import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BookStore")
        self.mainloop()

App()