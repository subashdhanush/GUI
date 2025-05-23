import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

tasks = []

def add_task():
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        tasks.pop(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

# UI elements
frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=20)

delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_button.pack()

root.mainloop()
