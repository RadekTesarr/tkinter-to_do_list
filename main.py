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
input_frame = Frame(root, bg=main_color)
input_frame.pack()
text_frame = Frame(root, bg=main_color)
text_frame.pack()
button_frame = Frame(root, bg=main_color)
button_frame.pack()

# Input frame
user_input = Entry(input_frame, width=35, borderwidth=3, font=main_font)
user_input.grid(row=0, column=0, padx=5, pady=5)
add_button = Button(input_frame, text="Přidat", borderwidth=2, font=main_font, bg=button_color)
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=10)

#Text frame
list_box = Listbox(text_frame, height=15, width=45, borderwidth=3, font=main_font)
list_box.grid(row=0, column=0)

# Button frame
remove_button = Button(button_frame, text="Odstranit položku", borderwidth=2, font=main_font, bg=button_color)
remove_button.grid(row=0, column=0, padx=2, pady=10)
clear_button = Button(button_frame, text="Smazat seznam", borderwidth=2, font=main_font, bg=button_color)
clear_button.grid(row=0, column=1,padx=2, pady=10)
save_button = Button(button_frame, text="Uložit seznam", borderwidth=2, font=main_font, bg=button_color)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=8)
quit_button = Button(button_frame, text="Zavřít", borderwidth=2, font=main_font, bg=button_color, command=root.destroy)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=8)

# Main cycle
root.mainloop()