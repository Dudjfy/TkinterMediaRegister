from enum import Enum
from tkinter import *
from tkinter import filedialog, ttk, messagebox
from PIL import ImageTk, Image

# Root setup
root = Tk()
root.title("Media Register")
root.geometry("470x330")

# List box
lst_box = Listbox(root, height=14, width=35, bd=2, relief=GROOVE)
lst_box.place(x=245, y=35)


def update_lst_box(items_data):
    """Updates the list box widget by deleting the previous values and inserting the current ones, doesn't return."""
    lst_box.delete(0, END)
    for item in items_data:
        lst_box.insert(END, item)


# Enum class for item states
class ItemStates(Enum):
    BOOKS = 0
    MOVIES = 1
    ALL = 2


# Items data class to work with the data
class ItemsData:
    """
    A class to represent the data list items hold.

    ...

    Attributes
    ----------
    books : list
        a complete list for the book values
    movies : list
        a complete list for the movie values
    all : list
        a complete list for all the values of all types

    Methods
    -------
    add_book(title, author, pages):
        Adds the book value to the book and all lists, updates list box.
    add_movie(title, director, length):
        Adds the movie value to the book and all lists, updates list box.
    change_state(state):
        Changes current state to the one specified, updates list box.
    get_items():
        Returns data lists according to the current state
    """

    def __init__(self):
        self.books = []
        self.movies = []
        self.all = []

        self.state = ItemStates.ALL

    def add_book(self, title, author, pages):
        """
        Given the input values (if the values are valid), concatenates the values to a book string,
        adds the book value to the book and all lists, updates list box.
        If the input isn't valid an error messagebox appears.
        """
        if len(title.strip()) > 1 and len(author.strip()) and pages > 0:
            book = f"{title} ({author}, {pages} pages)"
            self.books.append(book)
            self.all.append(book)
            update_lst_box(self.get_items())
        else:
            messagebox.showwarning("Missing values", "Missing or invalid values for title, author or amount of pages!")

    def add_movie(self, title, director, length):
        """
        Given the input values (if the values are valid), concatenates the values to a movie string,
        adds the movie value to the movies and all lists, updates list box.
        If the input isn't valid an error messagebox appears.
        """
        if len(title.strip()) > 1 and len(director.strip()) and length > 0:
            movie = f"{title} ({director}, {length} minutes)"
            self.movies.append(movie)
            self.all.append(movie)
            update_lst_box(self.get_items())
        else:
            messagebox.showwarning("Missing values", "Missing or invalid values for title, director or movie length!")

    def change_state(self, state):
        """Changes current state to the one specified, updates list box."""
        self.state = state
        update_lst_box(self.get_items())

    def get_items(self):
        """Returns data lists according to the current state."""
        if self.state == ItemStates.BOOKS:
            return self.books
        elif self.state == ItemStates.MOVIES:
            return self.movies
        else:
            return self.all


# Creates the items data object
items_data = ItemsData()

# Creates notebook
notebook = ttk.Notebook(root)
notebook.place(x=15, y=15)

# Creates tabs
books = Frame(notebook, width=220, height=220, bg="white")
movies = Frame(notebook, width=220, height=220, bg="white")

notebook.add(books, text="Add Books")
notebook.add(movies, text="Add Movies")

# Set positions for the widgets inside the tabs
positions = [
    (10, 20),
    (70, 20),
    (10, 45),
    (70, 45),
    (10, 70),
    (70, 70),
    (100, 170),
]

# Books widgets and vars
book_title = StringVar()
book_author = StringVar()
book_pages = IntVar()

book_widgets = {
    "books_title_lbl": Label(books, text="Title:", bg="white"),
    "books_title_e": Entry(books, width=16, bd=2, relief=GROOVE, textvariable=book_title),
    "books_author_lbl": Label(books, text="Author:", bg="white"),
    "books_author_e": Entry(books, width=16, bd=2, relief=GROOVE, textvariable=book_author),
    "books_page_lbl": Label(books, text="Pages:", bg="white"),
    "books_page_spn": Spinbox(books, from_=1, to=1000, width=14, bd=2, relief=GROOVE, textvariable=book_pages),
    "books_add_book_btn": Button(books,
                                 text="Add Book",
                                 relief=FLAT,
                                 command=lambda: items_data.add_book(book_title.get(), book_author.get(), book_pages.get())),
}

# Movie widgets and vars
movie_title = StringVar()
movie_director = StringVar()
movie_length = IntVar()

movie_widgets = {
    "movies_title_lbl": Label(movies, text="Title:", bg="white"),
    "movies_title_e": Entry(movies, width=16, bd=2, relief=GROOVE, textvariable=movie_title),
    "movies_director_lbl": Label(movies, text="Director:", bg="white"),
    "movies_director_e": Entry(movies, width=16, bd=2, relief=GROOVE, textvariable=movie_director),
    "movies_length_lbl": Label(movies, text="Length:", bg="white"),
    "movies_length_spn": Spinbox(movies, from_=1, to=1000, width=14, bd=2, relief=GROOVE, textvariable=movie_length),
    "movies_add_book_btn": Button(movies,
                                  text="Add Movie",
                                  relief=FLAT,
                                  command=lambda: items_data.add_movie(movie_title.get(), movie_director.get(), movie_length.get())),
}

# Places the widgets according to the positions
for widget_collection in [book_widgets.values(), movie_widgets.values()]:
    for coords, widget in enumerate(widget_collection):
        widget.place(x=positions[coords][0], y=positions[coords][1])

# Filters for the list inside a label frame
filters = LabelFrame(root, text="Show", pady=5)
filters.place(x=245, y=265)

# Radio-buttons to select filters
show_all = Radiobutton(filters, text="All", command=lambda: items_data.change_state(ItemStates.ALL), value=IntVar())
show_books = Radiobutton(filters, text="Books", command=lambda: items_data.change_state(ItemStates.BOOKS), value=IntVar())
show_movies = Radiobutton(filters, text="Movies", command=lambda: items_data.change_state(ItemStates.MOVIES), value=IntVar())
empty = Label(filters, width=5)
show_all.grid(column=0, row=0)
show_books.grid(column=1, row=0)
show_movies.grid(column=2, row=0)
empty.grid(column=3, row=0)
show_all.select()

mainloop()
