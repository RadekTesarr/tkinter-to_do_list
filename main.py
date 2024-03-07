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

# Main cycle
root.mainloop()