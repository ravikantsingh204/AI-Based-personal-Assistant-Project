from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.font as font

import requests
import re
import validators
import os
from urllib.parse import urlparse

root = Tk()
root.title("Download File from URL")
icon = PhotoImage(file='E:\\major project 2\\Download_file\\icon.png')
root.iconphoto(False, icon)
root.minsize(600, 500)
root.maxsize(600, 500)
HEIGHT = 500
WIDTH = 500
FONT = font.Font(family="Comic Sans MS", size="10", weight="bold")

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(
    Image.open(r"E:\\major project 2\\Download_file\\bg.png"))
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg="yellow", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.80, relheight=0.25, anchor="n")

label_up = Label(frame)
label_up.place(relwidth=1, relheight=1)

label1 = Label(frame, text="Enter the URL", font=FONT, bd=5,
               bg="#fc034e", highlightbackground="#d9138a", fg="black")
label1.place(relx=0.1, rely=0.1, relwidth=0.25, relheight=0.25)

label2 = Label(frame, text="Enter Filename", font=FONT, bd=5,
               bg="#fc034e", highlightbackground="#d9138a", fg="black")
label2.place(relx=0.1, rely=0.64, relwidth=0.25, relheight=0.25)


entry1 = Entry(frame, font=FONT, fg="#001a4d")
entry1.place(relx=0.54, rely=0.1, relwidth=0.4, relheight=0.25)


entry2 = Entry(frame, font=FONT, fg="#001a4d")
entry2.place(relx=0.54, rely=0.64, relwidth=0.4, relheight=0.25)


def download(url, name):

    valid = validators.url(url)
    # if the url is valid
    if (valid != True):
        messagebox.showerror("Invalid URL", "URL is invalid")
    # if the url is empty
    elif (url == ""):
        messagebox.showerror("No valid URL", "URL cannot be empty")
    else:
        response = requests.get(url, allow_redirects=True)
        rhead = response.headers['Content-Type']

        # if the url is downloadable
        if (canbedownloaded(rhead)):
            if (name == ""):
                a = urlparse(url)
                name = os.path.basename(a.path)
            file_data = rhead.split('/')
            ext = file_data[1]

            filename = name+'.'+ext
            open(filename, "wb").write(response.content)
            label_down['text'] = f"Your file {filename}\n has been downloaded successfully."

        else:
            label_down['text'] = "This file is invalid. It can not be downloaded."


def canbedownloaded(rhead):
    if 'text' in rhead.lower():
        return False
    if 'html' in rhead.lower():
        return False
    return True


def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    label_down['text'] = ""


button1 = Button(root, text="DOWNLOAD", font=FONT, bg="pink", fg="black", activeforeground="pink",
                 activebackground="black", command=lambda: download(entry1.get(), entry2.get()))
button1.place(relx=0.25, rely=0.4, relwidth=0.19, relheight=0.07)

button2 = Button(root, text="CLEAR", font=FONT, bg="pink", fg="black",
                 activeforeground="pink", activebackground="black", command=clear)
button2.place(relx=0.55, rely=0.4, relwidth=0.19, relheight=0.07)


lower_frame = Frame(root, bg="yellow", bd=10)
lower_frame.place(relx=0.5, rely=0.53, relwidth=0.8,
                  relheight=0.25, anchor="n")

label_down = Label(lower_frame, font=FONT, fg="#001a4d",
                   anchor="nw", justify="left", bd=4)
label_down.place(relwidth=1, relheight=1)

root.mainloop()