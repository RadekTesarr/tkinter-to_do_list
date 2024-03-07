from tkinter import *

# Main window
root = Tk()
root.title("Seznam úkolů")
root.minsize(400,500)
root.iconbitmap("icon.ico")
root.resizable(False, False)

# Font and color definition
main_font = ("Times New Roman", 12)
main_color = "#dd7f00"
button_color = "#e2cff4"
root.config(bg=main_color)

# Main cycle
root.mainloop()