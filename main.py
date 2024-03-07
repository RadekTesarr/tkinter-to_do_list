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

# Frames
input_frame = Frame(root, bg="white")
input_frame.pack()
text_frame = Frame(root, bg="gray")
text_frame.pack()
button_frame = Frame(root, bg="gray")
button_frame.pack()

# Input frame
user_input = Entry(input_frame, width=30, borderwidth=3, font=main_font)
user_input.grid(row=0, column=0)
add_button = Button(input_frame, text="Přidat", borderwidth=2, font=main_font, bg=button_color)
add_button.grid(row=0, column=1)

#Text frame
list_box = Listbox(text_frame, height=15, width=45, borderwidth=3, font=main_font)
list_box.grid(row=0, column=0)

# Button frame
remove_button = Button(button_frame, text="Odstranit položku", borderwidth=2, font=main_font, bg=button_color)
remove_button.grid(row=0, column=0)
clear_button = Button(button_frame, text="Smazat seznam", borderwidth=2, font=main_font, bg=button_color)
clear_button.grid(row=0, column=1)
save_button = Button(button_frame, text="Uložit seznam", borderwidth=2, font=main_font, bg=button_color)
save_button.grid(row=0, column=2)
quit_button = Button(button_frame, text="Zavřít", borderwidth=2, font=main_font, bg=button_color, command=root.destroy)
quit_button.grid(row=0, column=3)

# Main cycle
root.mainloop()