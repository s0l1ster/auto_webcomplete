from ast import Lambda
from concurrent.futures import thread
from tkinter import *
from customtkinter import *
import tkinter
from PIL import Image
from tkinter.font import Font
import rows_def
# import subprocess
# import os
# import threading


n =1
rows_def.number

root = CTk()
root.title('Auto')
root.geometry("200x200")

root.resizable(False, False)

next_icon = CTkImage(Image.open(r"C:\Users\Vasya\PycharmProjects\pythonProject5\icons\next_button.ico"), size=(24, 24))
reset_icon = CTkImage(Image.open(r"C:\Users\Vasya\PycharmProjects\pythonProject5\icons\reset_button.ico"), size=(24, 24))
copy_icon = CTkImage(Image.open(r"C:\Users\Vasya\PycharmProjects\pythonProject5\icons\copy_button.ico"), size=(24, 24))

def copy_script():
    f = open(r'scripts.txt', 'r')
    c = f.read()
    root.clipboard_append(c)


def run_auto():
    from subprocess import Popen
    Popen(["python", "just_right.py"])
    

root.iconbitmap(r"C:\Users\Vasya\PycharmProjects\pythonProject5\icons\Vasia_and_Illya_AutoProgram_icon.ico")
set_appearance_mode("dark")






def number1():
    global n
    n +=1
    
    

print("!!!!",rows_def.s)
print(n)


button_copy = CTkButton(root, text="Copy",
                        compound="left",
                        fg_color = "transparent",
                        border_color="#FFCC70",
                        border_width=2,
                        command=copy_script)
button_copy.pack(pady=10)

button_next = CTkButton(root, text="Next",  
                        compound="left",
                        fg_color = "transparent",
                        border_color="#FFCC70",
                        border_width=2,
                        command=lambda: [number1(),rows_def.g_next()])
button_next.pack(pady=10)

button_open_auto = CTkButton(root, text = "Run auto program",
                             compound = "left",
                             fg_color = "transparent",
                             border_color = "#FFCC70",
                             border_width = 2,
                             command = run_auto
                             )
button_open_auto.pack(pady = 10)

button_reset = CTkButton(root, text="Reset",  
                         compound="left", 
                         fg_color = "transparent",
                         border_color="#FFCC70",
                         border_width=2,
                         command=rows_def.reset_script)
button_reset.pack(pady=10)

label_row = CTkLabel(root,text =n)
label_row.pack()

root.mainloop()