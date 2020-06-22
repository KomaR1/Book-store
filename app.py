from tkinter import *
import backend

window = Tk()

label_1 = Label(window, text="Title")
label_1.grid(row=0, column=0)

label_2 = Label(window, text="Author")
label_2.grid(row=0, column=2)

label_3 = Label(window, text="Year")
label_3.grid(row=1, column=0)

label_4 = Label(window, text="ISBN")
label_4.grid(row=1, column=2)

title_text = StringVar()
entry_1 = Entry(window, textvariable=title_text)
entry_1.grid(row=0, column=1)

author_text = StringVar()
entry_2 = Entry(window, textvariable=author_text)
entry_2.grid(row=0, column=3)

year_text = StringVar()
entry_3 = Entry(window, textvariable=year_text)
entry_3.grid(row=1, column=1)

isbn_text = StringVar()
entry_4 = Entry(window, textvariable=isbn_text)
entry_4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll_bar = Scrollbar(window)
scroll_bar.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list1.yview)

button_1 = Button(window, text="View all", width=12)
button_1.grid(row=2, column=3)

button_2 = Button(window, text="Search entry", width=12)
button_2.grid(row=3, column=3)

button_3 = Button(window, text="Add entry", width=12)
button_3.grid(row=4, column=3)

button_4 = Button(window, text="Update selected", width=12)
button_4.grid(row=5, column=3)

button_5 = Button(window, text="Delete selected", width=12)
button_5.grid(row=6, column=3)

button_6 = Button(window, text="Close", width=12)
button_6.grid(row=7, column=3)

window.mainloop()
