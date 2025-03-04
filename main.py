import tkinter as tk
from tkinter import *
import os

def save_tasks():
    with open('tasks.txt', 'w') as file:
        tasks = listbox.get(0, END)
        for task in tasks:
            file.write(f"{task}\n")


def load_tasks():
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(END, task.strip())

def add_task():
    task_text = task_entry.get()
    if task_text:
        listbox.insert(END, task_text)
        task_entry.delete(0, END)
        save_tasks()  


def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        save_tasks()  
    except IndexError:
        pass

def clear_tasks():
    listbox.delete(0, END)
    save_tasks()  

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x600")  
root.resizable(False, False)  


Image_icon = PhotoImage(file="./Images/task.png")
root.iconphoto(True, Image_icon)

TopImage = PhotoImage(file="./Images/topbar.png")
Label(root, image=TopImage).pack(fill=X)

dockImage = PhotoImage(file="./Images/dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="./Images/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=340, y=25)

heading = Label(root, text="All Tasks", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

frame = Frame(root, bg="white")
frame.pack(pady=10, padx=10, fill=X)

task_entry = Entry(frame, font="arial 20", bd=0)
task_entry.pack(side=LEFT, padx=10, expand=True, fill=X)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=add_task)
button.pack(side=RIGHT)

frame1 = Frame(root, bd=3, bg="#32405b")
frame1.pack(pady=(10, 0), padx=10, fill=BOTH, expand=True)

listbox = Listbox(frame1, font=('aria', 12), bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

Delete_icon = PhotoImage(file="./Images/delete.png")
delete_button = Button(root, image=Delete_icon, bd=0, command=delete_task)
delete_button.pack(side=BOTTOM, pady=5)

clear_button = Button(root, text="DELETE ALL", font="arial 20 bold", bg="#ff5a5a", fg="#fff", bd=0, command=clear_tasks)
clear_button.pack(side=BOTTOM, pady=10)

load_tasks()

root.mainloop()