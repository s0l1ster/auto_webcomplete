from tkinter import *
from customtkinter import *
import tkinter
from PIL import Image
from tkinter.font import Font
import rows_def

rows_def.number

root = CTk()
root.title('Auto')
root.geometry("200x150")

root.resizable(False, False)

next_icon = CTkImage(Image.open(r"C:\Users\Vasya\PycharmProjects\pythonProject5\icons\next_button.ico"), size=(24, 24))
reset_icon = CTkImage(Image.open(r"C:\Users\Vasya\PycharmProjects\pythonProject5\icons\reset_button.ico"), size=(24, 24))
copy_icon = CTkImage(Image.open(r"C:\Users\Vasya\PycharmProjects\pythonProject5\icons\copy_button.ico"), size=(24, 24))

def copy_script():
    f = open(r'scripts.txt', 'r')
    c = f.read()
    root.clipboard_append(c)




root.iconbitmap(r"C:\Users\Vasya\PycharmProjects\pythonProject5\icons\Vasia_and_Illya_AutoProgram_icon.ico")
set_appearance_mode("dark")

button_copy = CTkButton(root, text="Copy",
                        compound="left",
                        fg_color = "transparent",
                        border_color="#FFCC70",
                        border_width=2,
                        command=copy_script)
button_copy.pack(pady=10)

button_next = CTkButton(root, text="Next",  compound="left", command=rows_def.g_next)
button_next.pack(pady=10)

button_reset = CTkButton(root, text="Reset",  compound="left", command=rows_def.reset_script)
button_reset.pack(pady=10)

root.mainloop()
