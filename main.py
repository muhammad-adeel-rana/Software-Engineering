import tkinter as tk
from tkinter import *

def add_task():
    task_text = task_entry.get()
    if task_text:
        listbox.insert(END, task_text)
        task_entry.delete(0, END)

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do-list")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

Image_icon = PhotoImage(file="./Images/task.png")
root.iconphoto(True, Image_icon)

TopImage = PhotoImage(file="./Images/topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="./Images/dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="./Images/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=340, y=25)

heading = Label(root, text="All Task", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=add_task)
button.place(x=300, y=4)

frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('aria', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

Delete_icon = PhotoImage(file="./Images/delete.png")
delete_button = Button(root, image=Delete_icon, bd=0, command=delete_task)
delete_button.pack(side=BOTTOM, pady=13)

root.mainloop()
