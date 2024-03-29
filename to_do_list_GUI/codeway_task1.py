import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")  
        self.tasks = {}  
        
        self.listbox = tk.Listbox(root, width=50, height=20)
        self.listbox.pack(pady=20)  
        
       
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack(fill=tk.X, expand=True)  
        
        mark_done_button = tk.Button(root, text="Mark as Done", command=self.mark_done)
        mark_done_button.pack(fill=tk.X, expand=True)  
        
        
        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack(fill=tk.X, expand=True)  
        
        
        update_button = tk.Button(root, text="Update Task", command=self.update_task)
        update_button.pack(fill=tk.X, expand=True)  
        
        
        self.update_listbox()

   
    def add_task(self):
        task = simpledialog.askstring("Task", "Enter a new task:")
        if task:  
            self.tasks[task] = False  
            self.update_listbox()  

    
    def mark_done(self):
        task = self.listbox.get(tk.ANCHOR)  
        if task:  
            self.tasks[task] = True  
            self.update_listbox()  

    
    def delete_task(self):
        task = self.listbox.get(tk.ANCHOR)
        if task:
            del self.tasks[task]  
            self.update_listbox() 

    
    def update_task(self):
        task = self.listbox.get(tk.ANCHOR)
        if task:
            new_task = simpledialog.askstring("Update Task", "Enter the updated task:")
            if new_task:
                
                self.tasks[new_task] = self.tasks.pop(task)
                self.update_listbox()  

   
    def update_listbox(self):
        self.listbox.delete(0, tk.END)  
        for task, done in self.tasks.items():  
            self.listbox.insert(tk.END, f"{'[Done] ' if done else ''}{task}")


if __name__ == "__main__":
    root = tk.Tk()  
    app = ToDoListGUI(root)  
    root.mainloop()  
