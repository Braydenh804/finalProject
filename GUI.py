import tkinter
from tkinter import *
import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO


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


def create_screen_controller():
    # Create a Tkinter Log In Window
    start_window = Tk()
    start_window.title("Entertainment Hub")
    start_window.geometry(f'{1035}x{1080}+{-10}+{0}')
    start_window.columnconfigure(0, weight=1)
    start_window.rowconfigure(1, weight=1)
    start_window.configure(bg='#333333')
    # Create a Controller for the screens
    screen_master = ScreenController(start_window)
    screen_master.grid(row=1, column=0, sticky='n')

    # Create a navigation bar
    nav_bar = Frame(start_window)
    nav_bar.grid(row=0, column=0)
    nav_bar.config(bg="#333333")
    search_movies_button = Button(nav_bar, text='Search For Movies', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16),
                                  command=lambda: search_movies_window())
    search_tv_button = Button(nav_bar, text='Search For TV Shows', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16),
                              command=lambda: search_tv_window())
    movie_watchlist_button = Button(nav_bar, text='View Your Movie Watchlist', bg="#0c2b59", fg='#FFFFFF',
                                    font=("Arial", 16), command=lambda: movie_watchlist_window())
    tv_watchlist_button = Button(nav_bar, text='View Your TV Watchlist', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16),
                                 command=lambda: tv_watchlist_window())
    sign_out_button = Button(nav_bar, text='Close App', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16), command=quit)

    # Placing toolbar widget
    search_movies_button.grid(row=0, column=0)
    search_tv_button.grid(row=0, column=1)
    movie_watchlist_button.grid(row=0, column=2)
    tv_watchlist_button.grid(row=0, column=3)
    sign_out_button.grid(row=0, column=4)


    # Search For Movies Page
    def search_movies_window():
        # Create Start Page GUI widgets
        movie_search_page = Screen(screen_master, "Movie Search Page")
        movie_search_page.config(bg="#333333")
        header_label = Label(movie_search_page, text="Search For A Movie", bg='#333333', fg="#0c2b59", font=("Arial", 30))
        search_label = Label(movie_search_page, text="Enter Movie Title", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        search_entry = Entry(movie_search_page, font=("Arial", 16))
        search_button = Button(movie_search_page, text="Search", bg="#0c2b59", fg="#FFFFFF", font=("Arial", 16), command=lambda: movie_search_results_window())
        filter_label = Label(movie_search_page, text="Filter For A Movie", bg='#333333', fg="#0c2b59", font=("Arial", 30))
        year_label = Label(movie_search_page, text="Movie Release Year", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        year_entry = Entry(movie_search_page, font=("Arial", 16), width=4)
        rating_label = Label(movie_search_page, text="Minium Rating (0-10)", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        rating_entry = Entry(movie_search_page, font=("Arial", 16), width=4)
        genre_label = Label(movie_search_page, text="              Select Up To 3 Genres Below", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        filter_button = Button(movie_search_page, text="Search", bg="#0c2b59", fg="#FFFFFF", font=("Arial", 16),
                               command=lambda: movie_search_results_window())
        # Defining a Variable To Dynamically Change the Label Based On The Selected Checkboxes
        current_genres_text = tk.StringVar()
        current_genres_text.set("None Currently Selected")
        current_genres_label = Label(movie_search_page, textvariable=current_genres_text, bg='#333333', fg="#FFFFFF", font=("Arial", 10))


        # Placing widgets on the start_screen
        header_label.grid(row=0, column=0, pady=5, padx=60)
        search_label.grid(row=1, column=0)
        search_entry.grid(row=2, column=0)
        search_button.grid(row=3, column=0)
        filter_label.grid(row=0, column=1, pady=5, padx=60)
        year_label.grid(row=1, column=1)
        year_entry.grid(row=1, column=1, sticky="e", padx=60)
        rating_label.grid(row=2, column=1)
        rating_entry.grid(row=2, column=1, sticky="e", padx=60)
        genre_label.grid(row=3, column=1)
        current_genres_label.grid(row=4, column=1)
        filter_button.grid(row=5, column=1, sticky="e", padx=80)
        def create_checkboxes():
            #  List of Movie Genres
            movie_genres = [
                "Adventure", "Fantasy", "Action", "Biography", "Documentary", "News",
                "Sport", "Romance", "Drama", "Family", "History", "Mystery", "Crime",
                "Comedy", "Musical", "Thriller", "Adult", "Western", "War", "Horror",
                "Animation", "Sci-Fi", "Film-Noir", "Talk-Show", "Reality-TV", "Game-Show"
            ]

            # Sort values alphabetically
            movie_genres.sort()

            # Create a dictionary to hold checkbox variables
            checkbox_vars = {}

            # Initialize row counter
            row_num = 5

            # Create checkboxes for each value in the sorted list
            for value in movie_genres:
                checkbox_vars[value] = tk.BooleanVar()
                current_genres_selected = []
                checkbox = tk.Checkbutton(movie_search_page, text=value, fg="#FFFFFF", font=("Arial", 14), bg="#333333", variable=checkbox_vars[value],
                                          command=lambda v=value: on_checkbox_toggle(v))
                checkbox.grid(row=row_num, column=1, sticky="W", padx=115)
                row_num += 1

            def on_checkbox_toggle(value):
                # This function will be called whenever a genre checkbox is toggled

                # Checks if there is already 3 genres.py selected
                if len(current_genres_selected)==3 and value not in current_genres_selected:
                    return  # Exit Function Early
                else:
                    # Removes the value is it already exists
                    if value in current_genres_selected:
                        current_genres_selected.remove(value)
                        new_text = ', '.join(str(element) for element in current_genres_selected)
                        current_genres_text.set(new_text)
                        # If No Genres Selected Add Text Stating That
                        if not current_genres_selected:
                            current_genres_text.set("None Currently Selected")
                    else:
                        # Add The New Genre To The Label
                        current_genres_selected.append(value)
                        new_text = ', '.join(str(element) for element in current_genres_selected)
                        current_genres_text.set(new_text)

        create_checkboxes()

    
    # Search For TV Shows Page
    def search_tv_window():
        # Create Start Page GUI widgets
        tv_search_page = Screen(screen_master, "TV Search Page")
        tv_search_page.config(bg="#333333")
        header_label = Label(tv_search_page, text="Search For A Show", bg='#333333', fg="#0c2b59",
                             font=("Arial", 30))
        search_label = Label(tv_search_page, text="Enter Show Title", bg='#333333', fg="#FFFFFF",
                             font=("Arial", 16))
        search_entry = Entry(tv_search_page, font=("Arial", 16))
        search_button = Button(tv_search_page, text="Search", bg="#0c2b59", fg="#FFFFFF", font=("Arial", 16),
                               command=lambda: tv_search_results_window())
        filter_label = Label(tv_search_page, text="Filter For A Show", bg='#333333', fg="#0c2b59",
                             font=("Arial", 30))
        year_label = Label(tv_search_page, text="Show Release Year", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        year_entry = Entry(tv_search_page, font=("Arial", 16), width=4)
        rating_label = Label(tv_search_page, text="Minium Rating (0-10)", bg='#333333', fg="#FFFFFF",
                             font=("Arial", 16))
        rating_entry = Entry(tv_search_page, font=("Arial", 16), width=4)
        genre_label = Label(tv_search_page, text="              Select Up To 3 Genres Below", bg='#333333',
                            fg="#FFFFFF", font=("Arial", 16))
        filter_button = Button(tv_search_page, text="Search", bg="#0c2b59", fg="#FFFFFF", font=("Arial", 16),
                               command=lambda: tv_search_results_window())
        # Defining a Variable To Dynamically Change the Label Based On The Selected Checkboxes
        current_genres_text = tk.StringVar()
        current_genres_text.set("None Currently Selected")
        current_genres_label = Label(tv_search_page, textvariable=current_genres_text, bg='#333333', fg="#FFFFFF",
                                     font=("Arial", 10))

        # Placing widgets on the start_screen
        header_label.grid(row=0, column=0, pady=5, padx=60)
        search_label.grid(row=1, column=0)
        search_entry.grid(row=2, column=0)
        search_button.grid(row=3, column=0)
        filter_label.grid(row=0, column=1, pady=5, padx=60)
        year_label.grid(row=1, column=1)
        year_entry.grid(row=1, column=1, sticky="e" , padx=63)
        rating_label.grid(row=2, column=1)
        rating_entry.grid(row=2, column=1, sticky="e", padx=63)
        genre_label.grid(row=3, column=1)
        current_genres_label.grid(row=4, column=1)
        filter_button.grid(row=5, column=1, sticky="e", padx=90)

        def create_checkboxes():
            #  List of TV_show Genres
            tv_genres = [
                "Adventure", "Fantasy", "Action", "Biography", "Documentary", "News",
                "Sport", "Romance", "Drama", "Family", "History", "Mystery", "Crime",
                "Comedy", "Musical", "Thriller", "Adult", "Western", "War", "Horror",
                "Animation", "Sci-Fi", "Film-Noir", "Talk-Show", "Reality-TV", "Game-Show"
            ]

            # Sort values alphabetically
            tv_genres.sort()

            # Create a dictionary to hold checkbox variables
            checkbox_vars = {}

            # Initialize row counter
            row_num = 5

            # Create checkboxes for each value in the sorted list
            for value in tv_genres:
                checkbox_vars[value] = tk.BooleanVar()
                current_genres_selected = []
                checkbox = tk.Checkbutton(tv_search_page, text=value, fg="#FFFFFF", font=("Arial", 14), bg="#333333",
                                          variable=checkbox_vars[value],
                                          command=lambda v=value: on_checkbox_toggle(v))
                checkbox.grid(row=row_num, column=1, sticky="W", padx=114)
                row_num += 1

            def on_checkbox_toggle(value):
                # This function will be called whenever a genre checkbox is toggled

                # Checks if there is already 3 genres.py selected
                if len(current_genres_selected) == 3 and value not in current_genres_selected:
                    return  # Exit Function Early
                else:
                    # Removes the value is it already exists
                    if value in current_genres_selected:
                        current_genres_selected.remove(value)
                        new_text = ', '.join(str(element) for element in current_genres_selected)
                        current_genres_text.set(new_text)
                        # If No Genres Selected Add Text Stating That
                        if not current_genres_selected:
                            current_genres_text.set("None Currently Selected")
                    else:
                        # Add The New Genre To The Label
                        current_genres_selected.append(value)
                        new_text = ', '.join(str(element) for element in current_genres_selected)
                        current_genres_text.set(new_text)

        create_checkboxes()

    # Function That Converts An Image Link Into Picture Usable In The GUI
    def resize_and_display_image_from_url(image_url, image_button):
        # Download the image from the URL
        response = requests.get(image_url)
        img_data = BytesIO(response.content)

        # Open the image from the downloaded data
        original_img = Image.open(img_data)

        # Resize the image
        new_size = (216, 336)  # Replace with the desired dimensions
        resized_img = original_img.resize(new_size)

        # Convert the resized image to Tkinter PhotoImage
        tk_img = ImageTk.PhotoImage(resized_img)

        # Update the label with the resized image
        image_button.configure(image=tk_img)
        image_button.image = tk_img


    def movie_search_results_window():
        pass



    def tv_search_results_window():
        tv_search_page = Screen(screen_master, "TV Search Results")
        tv_search_page.config(bg="#333333")


    def movie_watchlist_window():

        movie_watchlist_page = Screen(screen_master, "Movie Watchlist")
        movie_watchlist_page.config(bg="#333333")

        watchlist_label = Label(movie_watchlist_page, text="Your Movie Watchlist", bg='#333333', fg="#FFFFFF",
                             font=("Arial", 36))
        watchlist_label.grid(row=0, column=0, columnspan=2, pady=10, padx=300, sticky='w')


        url = "https://m.media-amazon.com/images/M/MV5BYTU3NWI5OGMtZmZhNy00MjVmLTk1YzAtZjA3ZDA3NzcyNDUxXkEyXkFqcGdeQXVyODY5Njk4Njc@._V1_FMjpg_UX1000_.jpg"

        watchlist_image_button1 = Button(movie_watchlist_page, text="Breaking Bad\nTV Series 2008-2013\n9.5/10 2.1M",
                                         image=None, compound=TOP, bg='#333333', borderwidth=0, fg='#FFFFFF',
                                         font=("Arial", 16), command=lambda: movie_info_window())
        watchlist_image_button1.grid(row=1,column=0, sticky='w', padx=225)
        img = resize_and_display_image_from_url(url, watchlist_image_button1)
        watchlist_image_button1.config(image=img)

        watchlist_image_button2 = Button(movie_watchlist_page, text="Breaking Bad\nTV Series 2008-2013\n9.5/10 2.1M",
                                         image=None, compound=TOP, bg='#333333', borderwidth=0, fg='#FFFFFF',
                                         font=("Arial", 16), command=lambda: movie_info_window())
        watchlist_image_button2.grid(row=1, column=0, sticky='w', padx=600)
        img = resize_and_display_image_from_url(url, watchlist_image_button2)
        watchlist_image_button2.config(image=img)
        wlist_back_button = Button(movie_watchlist_page, text="Reload Last",
                                         image=None, compound=TOP, bg='#0c2b59', borderwidth=0, fg='#FFFFFF', font=("Arial", 16))
        wlist_next_button = Button(movie_watchlist_page, text="Load Next",
                                   image=None, compound=TOP, bg='#0c2b59', borderwidth=0, fg='#FFFFFF',
                                   font=("Arial", 16))
        wlist_back_button.grid(row=2, column=0, sticky='w', padx=270)
        wlist_next_button.grid(row=2, column=0, sticky='w', padx=655)
        wlist_number_of_pages_label = Label(movie_watchlist_page, text= "1/2 pages", bg="#333333", fg="#FFFFFF", font=("Arial", 16), width=86)
        wlist_number_of_pages_label.grid(row=3, column=0, sticky='w')
    def tv_watchlist_window():
        tv_watchlist_page = Screen(screen_master, " Tv Watchlist")
        tv_watchlist_page.config(bg="#333333")
        watchlist_label = Label(tv_watchlist_page, text="Your Tv-Show Watchlist", bg='#333333', fg="#FFFFFF",
                                font=("Arial", 36))
        watchlist_label.grid(row=0, column=0, columnspan=2, pady=10, padx=258, sticky='w')

        url = "https://m.media-amazon.com/images/M/MV5BYTU3NWI5OGMtZmZhNy00MjVmLTk1YzAtZjA3ZDA3NzcyNDUxXkEyXkFqcGdeQXVyODY5Njk4Njc@._V1_FMjpg_UX1000_.jpg"

        watchlist_image_button1 = Button(tv_watchlist_page, text="Breaking Bad\nTV Series 2008-2013\n9.5/10 2.1M",
                                         image=None, compound=TOP, bg='#333333', borderwidth=0, fg='#FFFFFF',
                                         font=("Arial", 16), command=lambda: movie_info_window())
        watchlist_image_button1.grid(row=1, column=0, sticky='w', padx=225)
        img = resize_and_display_image_from_url(url, watchlist_image_button1)
        watchlist_image_button1.config(image=img)

        watchlist_image_button2 = Button(tv_watchlist_page, text="Breaking Bad\nTV Series 2008-2013\n9.5/10 2.1M",
                                         image=None, compound=TOP, bg='#333333', borderwidth=0, fg='#FFFFFF',
                                         font=("Arial", 16), command=lambda: movie_info_window())
        watchlist_image_button2.grid(row=1, column=0, sticky='w', padx=600)
        img = resize_and_display_image_from_url(url, watchlist_image_button2)
        watchlist_image_button2.config(image=img)
        wlist_back_button = Button(tv_watchlist_page, text="Reload Last",
                                   image=None, compound=TOP, bg='#0c2b59', borderwidth=0, fg='#FFFFFF',
                                   font=("Arial", 16))
        wlist_next_button = Button(tv_watchlist_page, text="Load Next",
                                   image=None, compound=TOP, bg='#0c2b59', borderwidth=0, fg='#FFFFFF',
                                   font=("Arial", 16))
        wlist_back_button.grid(row=2, column=0, sticky='w', padx=270)
        wlist_next_button.grid(row=2, column=0, sticky='w', padx=655)
        wlist_number_of_pages_label = Label(tv_watchlist_page, text="1/2 pages", bg="#333333", fg="#FFFFFF",
                                            font=("Arial", 16), width=86)
        wlist_number_of_pages_label.grid(row=3, column=0, sticky='w')


    def movie_info_window():
        movie_search_page = Screen(screen_master, "Movie Search Results")
        movie_search_page.config(bg="#333333")
        url = "https://m.media-amazon.com/images/M/MV5BYTU3NWI5OGMtZmZhNy00MjVmLTk1YzAtZjA3ZDA3NzcyNDUxXkEyXkFqcGdeQXVyODY5Njk4Njc@._V1_FMjpg_UX1000_.jpg"
        movie_details_img = Button(movie_search_page, text="TV Series 2008-2013\n9.5/10 2.1M", compound=TOP, img=None,
                                   borderwidth=0, bg='#333333', fg='#FFFFFF', font=("Arial", 16),)
        resize_and_display_image_from_url(url, movie_details_img)
        movie_details_img.grid(row=1, column=0, sticky="nw")
        movie_title = Label(movie_search_page, text="Breaking Bad", bg='#333333', fg="#FFFFFF", font=("Arial", 19))
        movie_title.grid(row=1, column=0, padx=225, pady=5, sticky="nw")
        rating_title = Label(movie_search_page, text="A chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing\nand selling methamphetamine with a former student in order to secure his family's\nfuture", bg='#333333', fg="#FFFFFF", font=("Arial", 16), borderwidth=0, pady=10)
        rating_title.grid(row=1, column=0, padx=225, pady=80, sticky="nw")
        movie_genre_tag1 = Button(movie_search_page, text="Documentary", font=("Arial", 14), bg='#0c2b59', fg='#FFFFFF', width=11, height=1)
        movie_genre_tag2 = Button(movie_search_page, text="Action", font=("Arial", 14), bg='#0c2b59', fg='#FFFFFF', width=11, height=1)
        movie_genre_tag3 = Button(movie_search_page, text="Documentary", font=("Arial", 14), bg='#0c2b59', fg='#FFFFFF', width=11, height=1)
        movie_genre_tag1.grid(row=1, column=0, padx=217, pady=45, sticky="nw")
        movie_genre_tag2.grid(row=1, column=0, padx=344, pady=45, sticky="nw")
        movie_genre_tag3.grid(row=1, column=0, padx=471, pady=45, sticky="nw")
        add_to_watch_list = Button(movie_search_page, text="Add to\nWatchlist", font=("Arial", 14), bg='#0c2b59', fg='#FFFFFF', width=11)
        add_to_watch_list.grid(row=2, column=0, sticky='nw')



    start_window.mainloop()


if __name__ == '__main__':
    create_screen_controller()
