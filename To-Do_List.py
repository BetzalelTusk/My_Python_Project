# This file was written in its ENTIRETY by OpenAI's ChatGPT

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.configure(bg="teal")
root.title("To-Do List")
root.geometry("400x400")  # standard size
root.resizable(True, True)  # resizable beyond and below standard
tasks = [""]


def add_task():
    task = entry.get()
    if task.strip():
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")


def delete_task():
    try:
        if tasks.length == 1:

            selected_index = listbox.curselection()[0]
            tasks.pop(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning(
            "Selection Error", "Please select a task to delete.")


def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)
    print(tasks)


entry = tk.Entry(root, width=40)  # this is where text is inserted
entry.pack(pady=10)  # sets the padding (Y)

add_button = tk.Button(root, text="add task", command=add_task)
add_button.pack(pady=10)

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="delete button",
                          command=delete_task, width=10)
delete_button.pack(pady=10)

root.mainloop()
