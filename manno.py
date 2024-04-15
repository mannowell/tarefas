import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Deletar Tarefa", command=self.delete_task)
        self.delete_button.pack()
        
        self.save_button = tk.Button(root, text="Salvar Lista", command=self.save_tasks)
        self.save_button.pack()

        self.load_button = tk.Button(root, text="Carregar Lista", command=self.load_tasks)
        self.load_button.pack()
        

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            new_task = Task(task_description)
            self.tasks.append(new_task)
            self.task_listbox.insert(tk.END, new_task.description)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Por favor, insira uma descrição para a tarefa.")
            

    def save_tasks(self):
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                for task in self.tasks:
                    f.write(f"{task.description}\n")
            messagebox.showinfo("Sucesso", "Lista de tarefas salva com sucesso!")

    def load_tasks(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
        if file_path:
            self.tasks.clear()
            self.task_listbox.delete(0, tk.END)
            with open(file_path, "r") as f:
                for line in f:
                    task_description = line.strip()
                    new_task = Task(task_description)
                    self.tasks.append(new_task)
                    self.task_listbox.insert(tk.END, new_task.description)
            messagebox.showinfo("Sucesso", "Lista de tarefas carregada com sucesso!")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.task_listbox.delete(index)
        else:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para deletar.")
            

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
