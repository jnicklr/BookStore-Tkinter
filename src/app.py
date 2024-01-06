from tkinter import *
from database import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.dataBase = DataBase()
        self.title("BookStore")
        self.createWidgets()
        self.mainloop()
        
    def createWidgets(self):
        # Labels and Entrys.
        titleLabel = Label(self, text="Title")
        titleLabel.grid(row=0, column=0)

        titleVar = StringVar()
        titleEntry = Entry(self, textvariable=titleVar)
        titleEntry.grid(row=0, column=1)

        authorLabel = Label(self, text="Author")
        authorLabel.grid(row=0, column=2)

        authorVar = StringVar()
        authorEntry = Entry(self, textvariable=authorVar)
        authorEntry.grid(row=0, column=3)

        yearLabel = Label(self, text="Year")
        yearLabel.grid(row=1, column=0)

        yearVar = StringVar()
        yearEntry = Entry(self, textvariable=yearVar)
        yearEntry.grid(row=1, column=1)

        isbnLabel = Label(self, text="ISBN")
        isbnLabel.grid(row=1, column=2)

        isbnVar = StringVar()
        isbnEntry = Entry(self, textvariable=isbnVar)
        isbnEntry.grid(row=1, column=3)

        # List of the items and the scrollbar.

        itemsList = Listbox(self, height=6, width=35)
        itemsList.grid(row=2, column=0, rowspan=6,columnspan=2)

        itemsListScrollbar = Scrollbar(self)
        itemsListScrollbar.grid(row=2, column=2, rowspan=6)

        itemsList.configure(yscrollcommand=itemsListScrollbar.set)
        itemsListScrollbar.configure(command=itemsList.yview)

        # Actions Buttons.

        viewButton = Button(self, text="View All", width=12)
        viewButton.grid(row=2, column=3)

        searchButton = Button(self, text="Search Entry", width=12)
        searchButton.grid(row=3, column=3)

        addButton = Button(self, text="Add Entry", width=12)
        addButton.grid(row=4, column=3)

        updateButton = Button(self, text="Update Entry", width=12)
        updateButton.grid(row=5, column=3)

        deleteButton = Button(self, text="Delete Entry", width=12)
        deleteButton.grid(row=6, column=3)

        closeButton = Button(self, text="Close", width=12)
        closeButton.grid(row=7, column=3)

App()