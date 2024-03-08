from tkinter import *

# Main window
root = Tk()
root.title("Seznam úkolů")
root.minsize(600,400)
root.iconbitmap("icon.ico")
root.resizable(False, False)

# Font and color definition
main_font = ("Times New Roman", 12)
main_color = "#dd7f00"
button_color = "#ffbe66"
root.config(bg=main_color)

# Funkction
def add_task():
    # add one item into lisbox
    list_box.insert(END, user_input.get())
    user_input.delete(0, END)

def remove_task_item():
    # remove one item in listbox
    list_box.delete(ANCHOR)

def clear_listbox():
    # remove all items from listbox
    list_box.delete(0, END)

def save_list():
    # save tasks into txt file
    with open("tasks.txt", "w") as task_file:
        my_tasks = list_box.get(0, END)
        for i in my_tasks:
            task_file.write(f"{i}\n")

# Frames
input_frame = Frame(root, bg=main_color)
input_frame.pack()
text_frame = Frame(root, bg=main_color)
text_frame.pack()
button_frame = Frame(root, bg=main_color)
button_frame.pack()

# Input frame
user_input = Entry(input_frame, width=35, borderwidth=3, font=main_font)
user_input.grid(row=0, column=0, padx=5, pady=5)
add_button = Button(input_frame, text="Přidat", borderwidth=2, font=main_font, bg=button_color, command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=10)

# Scrollbar
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky=N+S)

#Text frame
list_box = Listbox(text_frame, height=15, width=45, borderwidth=3, font=main_font, yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0)

# Scrollbar and listbox connect
text_scrollbar.config(command=list_box.yview)

# Button frame
remove_button = Button(button_frame, text="Odstranit položku", borderwidth=2, font=main_font, bg=button_color, command=remove_task_item)
remove_button.grid(row=0, column=0, padx=2, pady=10)
clear_button = Button(button_frame, text="Smazat seznam", borderwidth=2, font=main_font, bg=button_color, command=clear_listbox)
clear_button.grid(row=0, column=1,padx=2, pady=10)
save_button = Button(button_frame, text="Uložit seznam", borderwidth=2, font=main_font, bg=button_color, command=save_list)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=8)
quit_button = Button(button_frame, text="Zavřít", borderwidth=2, font=main_font, bg=button_color, command=root.destroy)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=8)


# Main cycle
root.mainloop()