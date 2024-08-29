import os, shutil, sys
from tkinter import *
import customtkinter
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox

root = customtkinter.CTk()
root.geometry("300x500")
root.title("File Sorter")
n = 0
def open_dir_selector():
    folder_path = filedialog.askdirectory()
    current_dir.set(folder_path)

def sort_files():
    global n
    current_dir.set(current_dir.get().replace("\\", "/"))
    try:
        for subdir, dir, files in os.walk(current_dir.get()):
            for element in files: #Select separator of name. for example: _ ; Space can be used
                try:
                    folders = element.split(separator.get())[int(prefix.get())]
                except IndexError:
                    CTkMessagebox(title="Error", message=f"Wrong prefix", icon="cancel")


                if not os.path.exists(f'{current_dir.get()}/{folders}'):
                    pass
                    os.mkdir(f'{current_dir.get()}/{folders}')

            for file in files:
                if file == 'desktop.ini':
                    continue
                shutil.move(current_dir.get() + '/' + file, current_dir.get() + '/' + file.split(separator.get())[int(prefix.get())] + '/' + file) #moving file
                n += 1

    except FileNotFoundError:
        CTkMessagebox(title="Files sorted", message=f"{n} have been sorted", icon="check")

#TK Variables
current_dir = StringVar()
separator = StringVar()
prefix = StringVar()
prefix.set("0")

#Tkinter Widgets
customtkinter.CTkButton(master=root, text="Select folder", command=open_dir_selector).place(relx=0.5, rely=0.1, anchor=CENTER)
customtkinter.CTkLabel(master=root, text="Directory path").place(relx=0.5, rely=0.2, anchor=CENTER)
customtkinter.CTkEntry(master=root, textvariable=current_dir).place(relx=0.5, rely=0.25, anchor=CENTER)
customtkinter.CTkLabel(master=root, text="Separator").place(relx=0.5, rely=0.35, anchor=CENTER)
customtkinter.CTkEntry(master=root, textvariable=separator).place(relx=0.5, rely=0.4, anchor=CENTER)
customtkinter.CTkLabel(master=root, text="Prefix").place(relx=0.5, rely=0.5, anchor=CENTER)
customtkinter.CTkEntry(master=root, textvariable=prefix).place(relx=0.5, rely=0.55, anchor=CENTER)
customtkinter.CTkButton(master=root, text="Sort files", command=sort_files).place(relx=0.5, rely=0.75, anchor=CENTER)



root.mainloop()