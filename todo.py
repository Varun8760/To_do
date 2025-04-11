import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("✅ To-Do List with Checkboxes")
root.geometry("400x500")
root.configure(bg="#f0f4ff")

tasks = []
task_vars = []
task_widgets = []

def refresh_tasks():
    for widget in task_widgets:
        widget.destroy()
    task_widgets.clear()

    for i, (text, var) in enumerate(tasks):
        cb = tk.Checkbutton(task_frame, text=text, variable=var, font=("Arial", 12),
                            bg="#f0f4ff", onvalue=True, offvalue=False,
                            command=lambda i=i: toggle_done(i), anchor='w', padx=10)
        cb.pack(fill='x', pady=2)
        task_widgets.append(cb)

def toggle_done(index):
    var = tasks[index][1]
    text = tasks[index][0]
    if var.get() and not text.startswith("✅"):
        tasks[index] = ("✅ " + text, var)
    elif not var.get() and text.startswith("✅"):
        tasks[index] = (text.replace("✅ ", "", 1), var)
    refresh_tasks()

def add_task(event=None): 
    text = entry.get().strip()
    if not text:
        return
    var = tk.BooleanVar()
    tasks.append((text, var))
    entry.delete(0, tk.END)
    refresh_tasks()

def delete_selected():
    to_delete = []
    for i, (_, var) in enumerate(tasks):
        if var.get():
            to_delete.append(i)
    for i in reversed(to_delete):
        tasks.pop(i)
    refresh_tasks()

tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f4ff").pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)
entry.bind("<Return>", add_task) 

btn_frame = tk.Frame(root, bg="#f0f4ff")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Delete Done", width=20, command=delete_selected).pack()

canvas = tk.Canvas(root, bg="#f0f4ff", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
task_frame = tk.Frame(canvas, bg="#f0f4ff")

task_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=task_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
scrollbar.pack(side="right", fill="y")

root.mainloop()
