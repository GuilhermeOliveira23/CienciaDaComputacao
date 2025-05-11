import tkinter as tk

# Criar uma janela
janela = tk.Tk()

# Configurar título da janela
janela.title("Minha Primeira Janela")

# Iniciar o loop principal da aplicação
janela.mainloop()


# Botão
def clique_botao():
  print("Botão clicado!")

janela = tk.Tk()
janela.title("Botão Simples")

# Criar um botão
botao = tk.Button(janela, text="Clique Aqui", command=clique_botao)
botao.pack()
janela.mainloop()


def mostrar_texto():
    texto = caixa_texto.get()
    label_texto.config(text=texto)

janela = tk.Tk()
janela.title("Entrada de Texto")

# Criar uma caixa de texto
caixa_texto = tk.Entry(janela)
caixa_texto.pack()

# Criar um botão para mostrar o texto
botao_mostrar = tk.Button(janela, text="Mostrar Texto", command=mostrar_texto)
botao_mostrar.pack()

# Criar uma label para exibir o texto
label_texto = tk.Label(janela)
label_texto.pack()

janela.mainloop()