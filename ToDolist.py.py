import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo List")
        self.root.geometry("300x400")
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)
        self.listbox = tk.Listbox(self.frame, width=30, height=10)
        self.listbox.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.entry = tk.Entry(self.frame, width=30)
        self.entry.pack(fill="x")
        self.add_button = tk.Button(self.frame, text="Add", command=self.add_item)
        self.add_button.pack(fill="x")

        self.delete_button = tk.Button(self.frame, text="Delete", command=self.delete_item)
        self.delete_button.pack(fill="x")

        self.clear_button = tk.Button(self.frame, text="Clear", command=self.clear_list)
        self.clear_button.pack(fill="x")

    def add_item(self):
        item = self.entry.get()
        if item:
            self.listbox.insert("end", item)
            self.entry.delete(0, "end")

    def delete_item(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except IndexError:
            messagebox.showerror("Error", "Select an item to delete")

    def clear_list(self):
        self.listbox.delete(0, "end")

root = tk.Tk()
app = ToDoList(root)
root.mainloop()
