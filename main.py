from enum import Enum
from tkinter import *
from tkinter import filedialog, ttk
from PIL import ImageTk, Image


root = Tk()
root.title("Media Register")
root.geometry("470x330")

lst_box = Listbox(root, height=14, width=35, bd=2, relief=GROOVE)
lst_box.place(x=245, y=35)


class ItemStates(Enum):
    BOOKS = 0
    MOVIES = 1
    ALL = 2


def update_lst_box(items_data):
    lst_box.delete(0, END)
    for item in items_data:
        lst_box.insert(END, item)


class ItemsData:
    def __init__(self):
        self.books = []
        self.movies = []
        self.all = []

        self.state = ItemStates.ALL
        self.tk_state = IntVar()
        self.tk_state.set(2)

    def add_book(self, title, author, pages):
        if len(title.strip()) > 1 and len(author.strip()) and pages > 0:
            book = f"{title} ({author}, {pages} pages)"
            self.books.append(book)
            self.all.append(book)
            update_lst_box(self.get_items())

    def add_movie(self, title, director, length):
        if len(title.strip()) > 1 and len(director.strip()) and length > 0:
            movie = f"{title} ({director}, {length} minutes)"
            self.movies.append(movie)
            self.all.append(movie)
            update_lst_box(self.get_items())

    def change_state(self, state):
        self.state = state
        update_lst_box(self.get_items())

    def get_items(self):
        if self.state == ItemStates.BOOKS:
            return self.movies
        elif self.state == ItemStates.MOVIES:
            return self.books
        else:
            return self.all


items_data = ItemsData()

# def insert_book(title, author, pages):
#     if len(title.strip()) > 1 and len(author.strip()) and pages > 0:
#         lst_box.insert(END, f"{title} ({author}, {pages} pages)")
#
#
# def insert_movie(title, director, length):
#     if len(title.strip()) > 1 and len(director.strip()) and length > 0:
#         lst_box.insert(END, f"{title} ({director}, {length} minutes)")


notebook = ttk.Notebook(root)
notebook.place(x=15, y=15)

books = Frame(notebook, width=220, height=220, bg="white")
movies = Frame(notebook, width=220, height=220, bg="white")

notebook.add(books, text="Add Books")
notebook.add(movies, text="Add Movies")

# Books widgets
positions = [
    (10, 20),
    (70, 20),
    (10, 45),
    (70, 45),
    (10, 70),
    (70, 70),
    (100, 170),
]

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

for widget_collection in [book_widgets.values(), movie_widgets.values()]:
    for coords, widget in enumerate(widget_collection):
        widget.place(x=positions[coords][0], y=positions[coords][1])

filters = LabelFrame(root, text="Show", pady=5)
filters.place(x=245, y=265)
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
