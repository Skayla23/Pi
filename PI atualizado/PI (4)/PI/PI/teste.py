import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Lookchic"
)
cursor = conexao.cursor()

def executar_query(query, dados=None):
    try:
        cursor.execute(query, dados)
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro ao executar a query: {e}")
        conexao.rollback()
        return False

def adicionar_produto(img_path, cor, produto_name, quant, preco_venda):
    try:
        img = Image.open(img_path)
        img.save("imagens/" + produto_name + ".png")

        query_produto = "INSERT INTO produto (img, cor, produto_name, quant, preco_venda) VALUES (%s, %s, %s, %s, %s)"
        dados_produto = ("imagens/" + produto_name + ".png", cor, produto_name, quant, preco_venda)
        executar_query(query_produto, dados_produto)

        return True
    except Exception as e:
        print(f"Erro ao adicionar produto: {e}")
        return False

def adicionar_produto_page():
    def adicionar_foto():
        path = filedialog.askopenfilename()
        if path:
            produto_entry = simpledialog.askstring("Informe o nome do produto", "Informe o nome do produto:S")
            img = Image.open(path)
            img = img.resize((100, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            img_label.config(image=img)
            img_label.image = img
            adicionar_produto_page.img_path = path

    def adicionar_preco():
        preco = simpledialog.askfloat("Informe o valor do produto", "Informe o valor do produto:")
        if preco is not None:
            adicionar_produto_page.preco_venda = preco
            preco_label.config(text=f"Preço: R${preco:.2f}")

    def adicionar_tamanho():
        tamanho = tamanho_combobox.get()
        adicionar_produto_page.tamanho = tamanho
        tamanho_label.config(text=f"Tamanho: {tamanho}")

    def adicionar_estoque():
        estoque = simpledialog.askinteger("Informe o estoque", "Informe a quantidade em estoque:")
        if estoque is not None:
            adicionar_produto_page.quant = estoque
            estoque_label.config(text=f"Estoque: {estoque}")

    def adicionar_cor():
        cor = simpledialog.askstring("Selecione a cor do produto", "Selecione a cor do produto:")
        if cor is not None:
            adicionar_produto_page.cor = cor
            cor_label.config(text=f"Cor: {cor}")

    def confirmar():
        if hasattr(adicionar_produto_page, 'img_path'):
            if adicionar_produto(adicionar_produto_page.img_path, adicionar_produto_page.cor, produto_entry.get(), adicionar_produto_page.quant, adicionar_produto_page.preco_venda):
                adicionar_produto_page.master.destroy()

    def cancelar():
        adicionar_produto_page.master.destroy()

    adicionar_produto_page.master = tk.Toplevel()
    adicionar_produto_page.master.title("Adicionar Produto")
    adicionar_produto_page.master.configure(bg="#FFC0CB")

    img_label = tk.Label(adicionar_produto_page.master, bg="#FFC0CB")
    img_label.grid(row=0, column=0, padx=10, pady=10)

    add_img_button = tk.Button(adicionar_produto_page.master, text="Adicionar Foto", command=adicionar_foto, bg="#FF69B4", fg="white")
    add_img_button.grid(row=1, column=0, pady=10)

    preco_label = tk.Label(adicionar_produto_page.master, text="Preço: R$0.00", bg="#FFC0CB")
    preco_label.grid(row=2, column=0, pady=10)

    add_preco_button = tk.Button(adicionar_produto_page.master, text="Preço", command=adicionar_preco, bg="#FF69B4", fg="white")
    add_preco_button.grid(row=3, column=0, pady=10)

    tamanhos = ["PP", "P", "M", "G"]
    tamanho_combobox = ttk.Combobox(adicionar_produto_page.master, values=tamanhos, state="readonly")
    tamanho_combobox.set("Selecione o tamanho")
    tamanho_combobox.grid(row=4, column=0, pady=10)

    tamanho_label = tk.Label(adicionar_produto_page.master, text="Tamanho: Nenhum", bg="#FFC0CB")
    tamanho_label.grid(row=5, column=0, pady=10)

    add_tamanho_button = tk.Button(adicionar_produto_page.master, text="Tamanho", command=adicionar_tamanho, bg="#FF69B4", fg="white")
    add_tamanho_button.grid(row=6, column=0, pady=10)

    estoque_label = tk.Label(adicionar_produto_page.master, text="Estoque: 0", bg="#FFC0CB")
    estoque_label.grid(row=7, column=0, pady=10)

    add_estoque_button = tk.Button(adicionar_produto_page.master, text="Estoque", command=adicionar_estoque, bg="#FF69B4", fg="white")
    add_estoque_button.grid(row=8, column=0, pady=10)

    cor_label = tk.Label(adicionar_produto_page.master, text="Cor: Nenhuma", bg="#FFC0CB")
    cor_label.grid(row=9, column=0, pady=10)

    add_cor_button = tk.Button(adicionar_produto_page.master, text="Cor", command=adicionar_cor, bg="#FF69B4", fg="white")
    add_cor_button.grid(row=10, column=0, pady=10)

    confirmar_button = tk.Button(adicionar_produto_page.master, text="Confirmar", command=confirmar, bg="#FF69B4", fg="white")
    confirmar_button.grid(row=11 , column=0, pady=10)

    cancelar_button = tk.Button(adicionar_produto_page.master, text="Cancelar", command=cancelar, bg="#FF69B4", fg="white")
    confirmar_button.grid(row=12 , column=0, pady=10)

    adicionar_produto_page.master.mainloop()

adicionar_produto_page()