import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            return f"Removed task: {removed_task}"
        else:
            return "Invalid task index!"

    def edit_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = new_task
            return "Task updated successfully!"
        else:
            return "Invalid task index!"

    def get_task_list(self):
        return self.tasks

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.todo_list = ToDoList()

        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Helvetica", 12))
        self.add_button.pack()

        self.task_list_frame = tk.Frame(root)
        self.task_list_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.update_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)

    def remove_task(self, task_index):
        result = self.todo_list.remove_task(task_index)
        self.update_listbox()
        messagebox.showinfo("Task Removal", result)

    def edit_task(self, task_index):
        new_task = simpledialog.askstring("Edit Task", "Enter the new task:")
        if new_task:
            result = self.todo_list.edit_task(task_index, new_task)
            self.update_listbox()
            messagebox.showinfo("Edit Task", result)

    def update_listbox(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        tasks = self.todo_list.get_task_list()
        for task_index, task in enumerate(tasks):
            task_frame = tk.Frame(self.task_list_frame, relief=tk.RIDGE, bd=1)
            task_label = tk.Label(task_frame, text=task, font=("Helvetica", 12), padx=10, pady=5)
            edit_button = tk.Button(task_frame, text="Edit", command=lambda i=task_index: self.edit_task(i), font=("Helvetica", 10))
            delete_button = tk.Button(task_frame, text="Delete", command=lambda i=task_index: self.remove_task(i), font=("Helvetica", 10))

            task_label.pack(side=tk.LEFT)
            edit_button.pack(side=tk.LEFT, padx=5)
            delete_button.pack(side=tk.LEFT)

            task_frame.pack(fill=tk.X, padx=10, pady=5)

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
