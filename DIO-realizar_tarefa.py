import speech_recognition as sr
import pywhatkit
from IPython.display import display, Markdown

#função para reconhecer a fala
def reconhecer_fala():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("🎤 Diga um comando financeiro...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR").lower()
        print(f"📝 Você disse: {comando}")
        return comando
    except sr.UnknownValueError:
        print("❌ Não entendi o que você disse.")
        return None
    except sr.RequestError:
        print("❌ Erro no serviço de reconhecimento.")
        return None

def calcular_juros_simples():
    valor = float(input("Valor inicial: "))
    taxa = float(input("Taxa (ex: 0.05): "))
    tempo = int(input("Tempo: "))

    resultado = valor * (1 + taxa * tempo)
    print(f"💰 Valor final: R$ {resultado:.2f}")

def calcular_juros_compostos():
    valor = float(input("Valor inicial: "))
    taxa = float(input("Taxa (ex: 0.05): "))
    tempo = int(input("Tempo: "))

    resultado = valor * (1 + taxa) ** tempo
    print(f"💰 Valor final: R$ {resultado:.2f}")

def executar_comando(comando):

    # 📊 Juros simples
    if "juros simples" in comando:
        print("📊 Calculando juros simples...")
        calcular_juros_simples()

    # 📈 Juros compostos
    elif "juros compostos" in comando:
        print("📈 Calculando juros compostos...")
        calcular_juros_compostos()

    # 🔍 Pesquisa financeira
    elif "pesquisar" in comando:
        termo = comando.replace("pesquisar", "").strip()
        if termo:
            display(Markdown(f"🔍 **Pesquisando:** {termo}"))
            pywhatkit.search(termo)
        else:
            print("❌ Nenhum termo informado.")

    # 💳 Explicações financeiras
    elif "o que é" in comando:
        termo = comando.replace("o que é", "").strip()
        if termo:
            display(Markdown(f"📚 **Buscando explicação sobre:** {termo}"))
            pywhatkit.search(f"{termo} finanças o que é")
        else:
            print("❌ Especifique o termo.")

    # 👋 Sair
    elif "sair" in comando:
        print("👋 Encerrando assistente financeiro...")
        return False

    else:
        print("❌ Comando não reconhecido.")

    return True

def main():
    print("💰 Assistente Financeiro iniciado!")
    
    rodando = True
    while rodando:
        comando = reconhecer_fala()
        if comando:
            rodando = executar_comando(comando)

if __name__ == "__main__":
    main()
