import speech_recognition as sr
import webbrowser
import sys

# Verifica se o PyAudio está instalado
try:
    import pyaudio
except:
    print("Instale o PyAudio primeiro: pip install pyaudio")
    sys.exit()

r = sr.Recognizer()

# Lista microfones disponíveis (para debug)
print("Microfones disponíveis:", sr.Microphone.list_microphone_names())

try:
    with sr.Microphone(device_index=0) as source:  # Tente outros índices se necessário
        print("Ajustando ruído... (aguarde 1 segundo)")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Diga algo!")
        audio = r.listen(source, timeout=5)  # Timeout de 5 segundos
        print("Processando áudio...")
        
        comando = r.recognize_google(audio, language='pt-BR').lower()
        print("Você disse:", comando)
        
        if "abrir youtube" in comando:
            webbrowser.open("https://youtube.com")
            print("YouTube aberto!")
        elif "pesquisar" in comando:
            query = comando.replace("pesquisar", "").strip()
            webbrowser.open(f"https://google.com/search?q={query}")
            print(f"Pesquisando: {query}")
        else:
            print("Comando não reconhecido.")

except sr.UnknownValueError:
    print("Não entendi o áudio. Repita, por favor!")
except sr.RequestError:
    print("Falha na conexão com o serviço de reconhecimento.")
except Exception as e:
    print("Erro inesperado:", str(e))