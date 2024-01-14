import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('To-Do List App')
        self.geometry("400x600") 
        self.tasks = []
        self.completed_tasks = []

        self.init_ui()

    def init_ui(self):
        # Task
        self.task_input = tk.Entry(self)
        self.task_input.grid(row=0, column=0, padx=10, pady=10)

        # Priority
        self.priority_var = tk.StringVar(self)
        self.priority_var.set("High")  # default value
        self.priority_dropdown = tk.OptionMenu(self, self.priority_var, "High", "Medium", "Low")
        self.priority_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Calendar for Due Date
        self.calendar = Calendar(self, selectmode='day')
        self.calendar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Task Button
        self.add_task_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=2, column=0, padx=10, pady=10)

        # Tasks List
        self.tasks_listbox = tk.Listbox(self, width=50, height=10)  # Increase the width and height of the listbox
        self.tasks_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Completed Tasks List
        self.completed_tasks_listbox = tk.Listbox(self, width=50, height=5)  # Create a listbox for completed tasks
        self.completed_tasks_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Complete Button
        self.complete_task_button = tk.Button(self, text="Mark Complete", command=self.complete_task)
        self.complete_task_button.grid(row=5, column=0, padx=10, pady=10)

        # Remove Completed Button
        self.remove_task_button = tk.Button(self, text="Remove Completed", command=self.remove_task)
        self.remove_task_button.grid(row=5, column=1, padx=10, pady=10)

    def add_task(self):
        task_name = self.task_input.get()
        if not task_name:
            messagebox.showwarning("Warning", "Please enter a task name.")
            return
        priority = self.priority_var.get()
        due_date = self.calendar.get_date()
        task_details = (task_name, priority, due_date)
        self.tasks.append(task_details)
        self.update_tasks_listbox()

    def complete_task(self):
        selected_indices = self.tasks_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Warning", "Please select a task to complete.")
            return
        for index in selected_indices:
            completed_task = self.tasks.pop(index)
            self.completed_tasks.append(completed_task)
        self.update_tasks_listbox()
        self.update_completed_tasks_listbox()

    def remove_task(self):
        selected_indices = self.completed_tasks_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Warning", "Please select a completed task to remove.")
            return
        for index in selected_indices:
            self.completed_tasks.pop(index)
        self.update_completed_tasks_listbox()

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, f"{task[0]} - Priority: {task[1]} - Due: {task[2]}")

    def update_completed_tasks_listbox(self):
        self.completed_tasks_listbox.delete(0, tk.END)
        for task in self.completed_tasks:
            self.completed_tasks_listbox.insert(tk.END, f"{task[0]} - Priority: {task[1]} - Due: {task[2]}")

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
