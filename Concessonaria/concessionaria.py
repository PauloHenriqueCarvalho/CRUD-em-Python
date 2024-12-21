import tkinter as tk
from tkinter import messagebox
from carros import Carros
from clientes import Clientes
from database import con 

class ConcessionariaApp:
    def __init__(self, root):
        self.db = con()  
        self.db_cursor = self.db.cursor()
        
        self.carros = Carros(self.db_cursor)
        self.clientes = Clientes(self.db_cursor)
        
        self.root = root
        self.root.title("Sistema de Concessionária")

        self.tela_login()

    def tela_login(self):
        self.clear_window()

        self.label_nome = tk.Label(self.root, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=10, pady=10)
        
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_senha = tk.Label(self.root, text="Senha:")
        self.label_senha.grid(row=1, column=0, padx=10, pady=10)

        self.entry_senha = tk.Entry(self.root, show="*")
        self.entry_senha.grid(row=1, column=1, padx=10, pady=10)

        self.btn_login = tk.Button(self.root, text="Login", command=self.login)
        self.btn_login.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()

        if nome and senha:
            cliente = self.clientes.login(nome, senha)
            if cliente:
                self.tela_carros(cliente) 
            else:
                messagebox.showerror("Erro", "Nome ou senha incorretos.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha ambos os campos.")

    def tela_carros(self, cliente):
        self.clear_window()

        self.label_carros = tk.Label(self.root, text="Carros no Estoque:")
        self.label_carros.grid(row=0, column=0, columnspan=2, pady=10)

        self.listbox_carros = tk.Listbox(self.root, height=10, width=50)
        self.listbox_carros.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.atualizar_lista_carros()

        self.btn_adicionar = tk.Button(self.root, text="Adicionar Carro", command=self.adicionar_carro)
        self.btn_adicionar.grid(row=2, column=0, pady=10)

        self.btn_remover = tk.Button(self.root, text="Remover Carro", command=self.remover_carro)
        self.btn_remover.grid(row=2, column=1, pady=10)

    def atualizar_lista_carros(self):
        self.listbox_carros.delete(0, tk.END)
        carros = self.carros.listarCarro()
        for carro in carros:
            self.listbox_carros.insert(tk.END, f"{carro[0]} - {carro[1]}")

    def adicionar_carro(self):
        def salvar_carro():
            marca = entry_marca.get()
            modelo = entry_modelo.get()
            preco = entry_preco.get()
            if marca and modelo:
                self.carros.adicionarCarro(marca, modelo,preco)
                messagebox.showinfo("Sucesso", f"Carro {marca} {modelo} {preco} adicionado ao estoque.")
                self.atualizar_lista_carros()
                adicionar_janela.destroy()
            else:
                messagebox.showerror("Erro", "Preencha ambos os campos.")

        adicionar_janela = tk.Toplevel(self.root)
        adicionar_janela.title("Adicionar Carro")

        label_marca = tk.Label(adicionar_janela, text="Marca:")
        label_marca.grid(row=0, column=0, padx=10, pady=10)

        entry_marca = tk.Entry(adicionar_janela)
        entry_marca.grid(row=0, column=1, padx=10, pady=10)

        label_modelo = tk.Label(adicionar_janela, text="Modelo:")
        label_modelo.grid(row=1, column=0, padx=10, pady=10)

        entry_modelo = tk.Entry(adicionar_janela)
        entry_modelo.grid(row=1, column=1, padx=10, pady=10)

        label_preco = tk.Label(adicionar_janela, text="Preco:")
        label_preco.grid(row=2, column=0, padx=10, pady=10)

        entry_preco = tk.Entry(adicionar_janela)
        entry_preco.grid(row=2, column=1, padx=10, pady=10) 

       



        btn_salvar = tk.Button(adicionar_janela, text="Salvar", command=salvar_carro)
        btn_salvar.grid(row=3, column=0, columnspan=2, pady=10)

    def remover_carro(self):
        selecionado = self.listbox_carros.curselection()
        if selecionado:
            carro = self.listbox_carros.get(selecionado)
            marca, modelo = carro.split(" - ")
            self.carros.removerCarro(marca, modelo)
            messagebox.showinfo("Sucesso", f"Carro {marca} {modelo} removido.")
            self.atualizar_lista_carros()
        else:
            messagebox.showerror("Erro", "Selecione um carro para remover.")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.grid_forget()

if __name__ == '__main__':
    root = tk.Tk()
    app = ConcessionariaApp(root)
    root.mainloop()
