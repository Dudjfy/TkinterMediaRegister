from tkinter import *
from tkinter import filedialog, ttk
from PIL import ImageTk, Image


root = Tk()
root.title("Media Register")
root.geometry("470x330")

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

book_widgets = {
    "books_title_lbl": Label(books, text="Title:", bg="white"),
    "books_title_e": Entry(books, width=16, bd=2, relief=GROOVE),
    "books_writer_lbl": Label(books, text="Writer:", bg="white"),
    "books_writer_e": Entry(books, width=16, bd=2, relief=GROOVE),
    "books_page_lbl": Label(books, text="Pages:", bg="white"),
    "books_page_spn": Spinbox(books, from_=1, to=1000, width=14, bd=2, relief=GROOVE),
    "books_add_book_btn": Button(books, text="Add Book", relief=FLAT),
}

movie_widgets = {
    "movies_title_lbl": Label(movies, text="Title:", bg="white"),
    "movies_title_e": Entry(movies, width=16, bd=2, relief=GROOVE),
    "movies_director_lbl": Label(movies, text="Director:", bg="white"),
    "movies_director_e": Entry(movies, width=16, bd=2, relief=GROOVE),
    "movies_length_lbl": Label(movies, text="Length:", bg="white"),
    "movies_length_spn": Spinbox(movies, from_=1, to=1000, width=14, bd=2, relief=GROOVE),
    "movies_add_book_btn": Button(movies, text="Add Movie", relief=FLAT),
}

for widget_collection in [book_widgets.values(), movie_widgets.values()]:
    for coords, widget in enumerate(widget_collection):
        widget.place(x=positions[coords][0], y=positions[coords][1])

lst_box = Listbox(root, height=14, width=35, bd=2, relief=GROOVE)
lst_box.place(x=245, y=35)

filters = LabelFrame(root, text="Show", padx=92, pady=10)
filters.place(x=245, y=265)
Label(filters, text="Hey").pack()

mainloop()
