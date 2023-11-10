import tkinter
from tkinter import *


class Screen(Frame):

    def __init__(self, master, name):
        Frame.__init__(self, master)
        # Attributes
        self.master = master
        self.name = name
        # Initalise with master
        self.master.add_screen(self)

    def show(self):
        """
        Method will show screen
        """
        self.master.show_screen(self.name)


class ScreenController(Frame):
    """
    Screen Controller
    will manage screens
    in the program
    """

    def __init__(self, parent):
        Frame.__init__(self, parent)
        # Configure
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Attributes
        self.allScreens = {}
        self.currentScreen = None

    def add_screen(self, screen_object):
        """
        Adds a Screen object to the screenController
        """
        # Place the screen
        screen_object.grid(row=0, column=0, sticky="nsew")
        # Add to dictionary
        self.allScreens[screen_object.name] = screen_object

    def show_screen(self, screen_name):
        if screen_name in self.allScreens:
            # Display
            self.allScreens[screen_name].tkraise()
            # Update variable
            self.currentScreen = screen_name

def create_start_window():
    # Create a Tkinter Log In Window
    start_window = Tk()
    start_window.title("Entertainment Hub")
    start_window.geometry(f'{1035}x{1080}+{-10}+{0}')
    start_window.columnconfigure(0, weight=1)
    start_window.rowconfigure(1, weight=1)
    start_window.configure(bg='#333333')
    # Create a Controller for the screens
    screen_master = ScreenController(start_window)
    screen_master.grid(row=1, column=0, sticky="N")

    # Login in window functions


    # Create Start Page GUI widgets
    start_page = Screen(screen_master, "Start Page")
    start_page.config(bg="#333333")
    header_label = Label(start_page, text="Search For A Movie", bg='#333333', fg="#0c2b59", font=("Arial", 30))
    search_label = Label(start_page, text="Enter Movie Title", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    search_entry = Entry(start_page, font=("Arial", 16))
    start_button = Button(start_page, text="Search", bg="#0c2b59", fg="#FFFFFF", font=("Arial", 16))
    filter_label = Label(start_page, text="Filter For A Movie", bg='#333333', fg="#0c2b59", font=("Arial", 30))
    year_label = Label(start_page, text="Movie Release Year", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    year_entry = Entry(start_page, font=("Arial", 16), width=4)


    # Placing widgets on the start_screen
    header_label.grid(row=0, column=0, columnspan=2, pady=20, padx=60)
    search_label.grid(row=1, column=0, columnspan=2)
    search_entry.grid(row=2, column=0, columnspan=2)
    start_button.grid(row=3, column=0, columnspan=2, pady=10)
    filter_label.grid(row=0, column=2, columnspan=2, pady=20, padx=60)
    year_label.grid(row=1, column=2)
    year_entry.grid(row=1, column=2, sticky="e")
    # Create a navigation bar
    nav_bar = Frame(start_window)
    nav_bar.grid(row=0, column=0)
    nav_bar.config(bg="#333333")
    search_movies_button = Button(nav_bar, text='Search For Movies', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16))
    search_tv_button = Button(nav_bar, text='Search For TV Shows', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16))
    watchlist_button = Button(nav_bar, text='View Your Watchlist', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16))
    sign_out_button = Button(nav_bar, text='Close', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16), command=quit)


    # Placing toolbar widgets
    search_movies_button.grid(row=0, column=0)
    search_tv_button.grid(row=0, column=1)
    watchlist_button.grid(row=0, column=2)
    sign_out_button.grid(row=0, column=3)
    start_window.mainloop()


if __name__ == '__main__':
    create_start_window()
