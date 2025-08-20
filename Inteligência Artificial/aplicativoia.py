import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import webbrowser
import os

class VoiceApp:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Assistente por Voz")
        self.root.geometry("400x300")
        
        # Botão para ativar o microfone
        self.btn_listen = tk.Button(
        root, 
        text="🎤 Falar", 
        command=self.listen_microphone,
        font=("Arial", 14, "bold"),
        bg="#3498db",  # Cor de fundo
        fg="white",    # Cor do texto
        activebackground="#2980b9",  # Cor quando clicado
        padx=20,       # Espaçamento horizontal
        pady=10,       # Espaçamento vertical
        borderwidth=0,  # Remove a borda padrão
        relief="flat",  # Estilo da borda
        cursor="hand2"  # Cursor de mão ao passar o mouse
)
        self.btn_listen.pack(pady=50)
        
        # Label para mostrar o resultado
        self.lbl_result = tk.Label(root, text="", font=("Arial", 12))
        self.lbl_result.pack()
        
        # Configura o reconhecedor de voz
        self.recognizer = sr.Recognizer()

        
    
    def listen_microphone(self):
        try:
            with sr.Microphone() as source:
                self.lbl_result.config(text="Ajustando ruído... (aguarde 1 segundo)")
                self.root.update()  # Atualiza a interface
                
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                self.lbl_result.config(text="Diga algo!")
                self.root.update()
                
                audio = self.recognizer.listen(source, timeout=5)
                self.lbl_result.config(text="Processando...")
                self.root.update()
                
                command = self.recognizer.recognize_google(audio, language='pt-BR').lower()
                self.lbl_result.config(text=f"Você disse: {command}")
                self.process_command(command)
                
        except sr.UnknownValueError:
            messagebox.showerror("Erro", "Não entendi o áudio. Repita, por favor!")
        except sr.RequestError:
            messagebox.showerror("Erro", "Falha na conexão com o serviço de reconhecimento.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {str(e)}")
    
    def process_command(self, command):
        if "youtube" in command:
            webbrowser.open("https://youtube.com")
        elif "abrir calculadora" in command:
            os.system("calc.exe")
        elif "desligar" in command:
            os.system("shutdown /s /t 0")
        elif "horas" in command:
            from datetime import datetime
            self.lbl_result.config(text=f"São {datetime.now().strftime('%H:%M')}")
        else:
            self.lbl_result.config(text="Comando não reconhecido. Tente 'abrir youtube' ou 'que horas são'.")

# Cria a janela principal
root = tk.Tk()
app = VoiceApp(root)
root.mainloop()