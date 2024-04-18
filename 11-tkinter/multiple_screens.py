from tkinter import Tk, Frame, Button, Label


class LoginFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text="LOGIN")
        self.label.grid(row=0, column=0)
        self.btn = Button(self, text="Login", command=parent.show_catalog)
        self.btn.grid(row=1, column=0)


class CatalogFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text="Catalog")
        self.label.grid(row=0, column=0)
        self.btn = Button(self, text="View", command=parent.show_details)
        self.btn.grid(row=1, column=0)
        self.btn_back = Button(self, text="Back", command=parent.show_login)
        self.btn_back.grid(row=2, column=0)


class DetailsFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text="Details")
        self.label.grid(row=0, column=0)
        self.btn_back = Button(self, text="Back", command=parent.show_catalog)
        self.btn_back.grid(row=1, column=0)


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.login_frame = LoginFrame(self)
        self.catalog_frame = CatalogFrame(self)
        self.details_frame = DetailsFrame(self)
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        self.catalog_frame.grid(row=0, column=0, sticky="nsew")
        self.details_frame.grid(row=0, column=0, sticky="nsew")
        self.show_login()

    def show_login(self):
        self.login_frame.tkraise()

    def show_catalog(self):
        self.catalog_frame.tkraise()

    def show_details(self):
        self.details_frame.tkraise()


window = Window()
window.mainloop()
