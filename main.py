from tkinter import *
from tkinter import filedialog, ttk
from PIL import ImageTk, Image


root = Tk()
root.title("Media Register")

notebook = ttk.Notebook(root)
notebook.pack(padx=15, pady=15, expand=True)

books = Frame(notebook, width=220, height=220, bg="white")
movies = Frame(notebook, width=220, height=220, bg="white")

notebook.add(books, text="Add Books")
notebook.add(movies, text="Add Movies")

# Books widgets
Label(books, bg="white").grid(column=0, row=0)

books_title_lbl = Label(books, text="Title:", bg="white")
books_title_e = Entry(books, width=16, bd=2, relief=GROOVE)
books_title_lbl.grid(column=0, row=1, sticky=W, padx=10, pady=2)
books_title_e.grid(column=1, row=1, sticky=W)

books_writer_lbl = Label(books, text="Writer:", bg="white")
books_writer_e = Entry(books, width=16, bd=2, relief=GROOVE)
books_writer_lbl.grid(column=0, row=2, sticky=W, padx=10, pady=2)
books_writer_e.grid(column=1, row=2, sticky=W)

books_page_lbl = Label(books, text="Pages:", bg="white")
books_page_spn = Spinbox(books, from_=1, to=1000, width=14, bd=2, relief=GROOVE)
books_page_lbl.grid(column=0, row=3, sticky=W, padx=10, pady=2)
books_page_spn.grid(column=1, row=3, sticky=W)

Label(books, bg="white").grid(column=0, row=4)
Label(books, bg="white").grid(column=0, row=5)
Label(books, bg="white").grid(column=0, row=6)


books_add_book_btn = Button(books, text="Add Book", relief=FLAT)
books_add_book_btn.grid(column=1, row=7, sticky=SE)

# Movies widgets
# Label(movies, text="lol", bg="white").place(x=100, y=100)
#
# movies_title_lbl = Label(movies, text="Title:", bg="white")
# movies_title_e = Entry(movies, width=16, bd=2, relief=GROOVE)
# movies_title_lbl.grid(column=0, row=1, sticky=W, padx=10, pady=2)
# movies_title_e.grid(column=1, row=1, sticky=W)
#
# movies_director_lbl = Label(movies, text="Director:", bg="white")
# movies_director_e = Entry(movies, width=16, bd=2, relief=GROOVE)
# movies_director_lbl.grid(column=0, row=2, sticky=W, padx=10, pady=2)
# movies_director_e.grid(column=1, row=2, sticky=W)
#
# movies_length_lbl = Label(movies, text="Length:", bg="white")
# movies_length_spn = Spinbox(movies, from_=1, to=300, width=14, bd=2, relief=GROOVE)
# movies_length_lbl.grid(column=0, row=3, sticky=W, padx=10, pady=2)
# movies_length_spn.grid(column=1, row=3, sticky=W)
#
# Label(movies, bg="white").grid(column=0, row=4)
# Label(movies, bg="white").grid(column=0, row=5)
# Label(movies, bg="white").grid(column=0, row=6)
#
#
# movies_add_book_btn = Button(movies, text="Add Book", relief=FLAT)
# books_add_book_btn.grid(column=1, row=7, sticky=SE)


mainloop()
