import tkinter as tk
from tkinter import simpledialog, messagebox

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caderno de Anotações")
        self.notes = {}

        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Adicionar Nota", command=self.add_note)
        self.add_button.pack()
        
        self.view_button = tk.Button(root, text="Visualizar Nota", command=self.view_note)
        self.view_button.pack()
        
        self.delete_button = tk.Button(root, text="Excluir Nota", command=self.delete_note)
        self.delete_button.pack()
    
    def add_note(self):
        title = simpledialog.askstring("Nova Nota", "Título da Nota:")
        if title:
            content = simpledialog.askstring("Conteúdo da Nota", "Digite sua anotação:")
            if content:
                self.notes[title] = content
                self.listbox.insert(tk.END, title)
    
    def view_note(self):
        selected = self.listbox.curselection()
        if selected:
            title = self.listbox.get(selected[0])
            content = self.notes[title]
            messagebox.showinfo(title, content)
    
    def delete_note(self):
        selected = self.listbox.curselection()
        if selected:
            title = self.listbox.get(selected[0])
            del self.notes[title]
            self.listbox.delete(selected[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
