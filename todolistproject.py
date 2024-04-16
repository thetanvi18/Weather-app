import tkinter as tk
from tkinter import ttk, messagebox

tasks = []

def add_task():
    task_data = task_field.get()
    if task_data:
        tasks.append(task_data)
        list_update()
        task_field.delete(0, 'end')
    else:
        messagebox.showinfo("Error", "Field is Empty")

def list_update():
    task_listbox.delete(0, 'end')
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except IndexError:
        messagebox.showinfo("Error", "No tasks Selected. Cannot Delete.")

def delete_all_tasks():
    if messagebox.askyesno("Delete All", "Are you sure?"):
        task_listbox.delete(0, 'end')
        tasks.clear()

def close():
    print(tasks)
    window.destroy()

window = tk.Tk()
window.title("To-Do List")
window.geometry("600x500")
window.resizable(0, 0)
window.configure(bg="#bf9278")

header_frame = tk.Frame(window, bg="#bf9278")
functions_frame = tk.Frame(window, bg="#bf9278")
listbox_frame = tk.Frame(window, bg="#bf9278")

header_frame.pack(fill="both")
functions_frame.pack(side="left", expand=True, fill="both")
listbox_frame.pack(side="right", expand=True, fill="both")

ttk.Label(header_frame, text="Your To-Do List", font=("Pristina", 40, "bold"), background="#bf9278", foreground="#fff").pack(padx=20, pady=10)

ttk.Label(functions_frame, text="Enter the Task : ", font=("Baskerville Old Face", 15), background="#bf9278", foreground="#000000").place(x=30, y=40)

task_field = ttk.Entry(functions_frame, font=("Baskerville Old Face", 15), width=18, background="#bf9278", foreground="#bf9278")
task_field.place(x=30, y=80)

ttk.Button(functions_frame, text="Add Task", width=24, command=add_task).place(x=40, y=120)
ttk.Button(functions_frame, text="Delete Task", width=24, command=delete_task).place(x=40, y=160)
ttk.Button(functions_frame, text="Delete All Tasks", width=24, command=delete_all_tasks).place(x=40, y=200)
ttk.Button(functions_frame, text="Exit", width=24, command=close).place(x=40, y=240)

style = ttk.Style()
style.configure("TListbox", background="FFF", foreground="#000", selectbackground="#cce072", selectforeground="#FFFFFF")

task_listbox = tk.Listbox(listbox_frame, width=26, height=13, selectmode='SINGLE', background="#FFFFFF", foreground="#000000", selectbackground="#cce072", selectforeground="#000", font=("Baskerville Old Face", 14))
task_listbox.place(x=10, y=20)

window.mainloop()
