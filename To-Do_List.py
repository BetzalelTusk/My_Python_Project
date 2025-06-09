import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.resizable(True, True)
tasks = []


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


entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="add task", command=add_task)
add_button.pack(pady=10)

listbox = tk.Listbox(root, width=10)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="delete button", command=delete_task)
delete_button.pack(pady=10)

root.mainloop()
