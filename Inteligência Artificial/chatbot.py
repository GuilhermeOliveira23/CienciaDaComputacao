import tkinter as tk
from tkinter import scrolledtext
import requests
import threading
import json  # Adicionado para processar streaming

class Phi3CoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phi-3 3.8B - Assistente de Código")
        self.root.geometry("800x600")

        # Área de chat
        self.chat_history = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            width=80,
            height=25,
            font=("Consolas", 10)
        )
        self.chat_history.pack(pady=10)

        # Frame de entrada
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        # Campo de entrada
        self.user_input = tk.Entry(
            input_frame,
            width=70,
            font=("Arial", 12)
        )
        self.user_input.pack(side=tk.LEFT, padx=5)
        self.user_input.bind("<Return>", self.enviar_pergunta)

        # Botão de envio
        self.btn_enviar = tk.Button(
            input_frame,
            text="Enviar",
            command=self.enviar_pergunta,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12)
        )
        self.btn_enviar.pack(side=tk.LEFT)

        # Configurações do Ollama
        self.ollama_url = "http://localhost:11434/api/generate"
        self.modelo = "phi3:3.8b"

    def enviar_pergunta(self, event=None):
        pergunta = self.user_input.get().strip()
        if not pergunta:
            return

        self.mostrar_mensagem("Você", pergunta)
        self.user_input.delete(0, tk.END)
        self.btn_enviar.config(state=tk.DISABLED)

        threading.Thread(
            target=self.obter_resposta,
            args=(pergunta,),
            daemon=True
        ).start()

    def obter_resposta(self, pergunta):
        try:
            dados = {
                "model": self.modelo,
                "prompt": pergunta,
                "stream": False,  # Desativado para evitar problemas no JSON
                "options":{
                    "num_ctx": 1024,
                    "temperature": 0.7,
                    "OLLAMA_NO_CUDA":1
                }
            }
            resposta = requests.post(
                self.ollama_url,
                json=dados,
                headers={"Content-Type": "application/json"},
                timeout=180  # Aumenta o timeout para modelos maiores
            )
            
            if resposta.status_code == 200:
                texto_resposta = resposta.json().get("response", "Sem resposta")
                self.mostrar_mensagem("Phi-3", texto_resposta)
            else:
                self.mostrar_mensagem("Erro", f"API retornou código {resposta.status_code}")
        
        except requests.exceptions.RequestException as e:
            self.mostrar_mensagem("Erro", f"Falha na conexão: {str(e)}")
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Erro inesperado: {str(e)}")
        finally:
            self.root.after(0, lambda: self.btn_enviar.config(state=tk.NORMAL))

    def mostrar_mensagem(self, remetente, mensagem):
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, f"{remetente}: {mensagem}\n\n")
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Phi3CoderApp(root)
    root.mainloop()