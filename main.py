from tkinter import *
import customtkinter

# Main window
root = customtkinter.CTk()
root.title("Seznam úkolů")
root.geometry("600x430")
root.iconbitmap("icon.ico")
root.resizable(False, False)

# Font and color definition
main_font = ("Arial", 12)
main_color = "#dd7f00"
button_color = "#ffbe66"


# Function
def add_task():
    # add one item into listbox
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
            if i.endswith("\n"):
                task_file.write(f"{i}")
            else:
                task_file.write(f"{i}\n")


def open_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for one_line in file:
                list_box.insert(END, one_line)
    except:
        print("Chyba")


# Frames
input_frame = customtkinter.CTkFrame(root)
input_frame.pack(pady=5)
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=5)
button_frame = customtkinter.CTkFrame(root)
button_frame.pack()

# Input frame
user_input = customtkinter.CTkEntry(input_frame, width=400)
user_input.grid(row=0, column=0, padx=5, pady=5)
add_button = customtkinter.CTkButton(input_frame, text="Přidat", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=10)

# Scrollbar
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky=N + S)

# Text frame
list_box = Listbox(text_frame, height=15, width=60, borderwidth=3, font=main_font, yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0)

text_scrollbar.config(command=list_box.yview)

# Button frame
remove_button = customtkinter.CTkButton(button_frame, text="Odstranit položku", command=remove_task_item)
remove_button.grid(row=0, column=0, padx=2, pady=5)
clear_button = customtkinter.CTkButton(button_frame, text="Smazat seznam", command=clear_listbox)
clear_button.grid(row=0, column=1, padx=2, pady=5)
save_button = customtkinter.CTkButton(button_frame, text="Uložit seznam", command=save_list)
save_button.grid(row=0, column=2, padx=2, pady=5)
quit_button = customtkinter.CTkButton(button_frame, text="Zavřít", command=root.destroy)
quit_button.grid(row=0, column=3, padx=2, pady=5)

# Load tasks to listbox
open_tasks()

# Main cycle
root.mainloop()
