import tkinter as tk
from tkinter import ttk, messagebox
import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# Carrega variável de ambiente da API
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Lista fixa de moedas suportadas no plano gratuito
moedas = {
    "USD": "Dólar Americano",
    "BRL": "Real Brasileiro",
    "EUR": "Euro",
    "GBP": "Libra Esterlina",
    "JPY": "Iene Japonês",
    "AUD": "Dólar Australiano",
    "CAD": "Dólar Canadense",
    "CHF": "Franco Suíço",
    "ARS": "Peso Argentino"
}

# Função para buscar cotações
cotacoes = {}
timestamp = None

def buscar_cotacoes():
    global cotacoes, timestamp
    try:
        moedas_str = ",".join(moedas.keys())
        url = f"http://api.currencylayer.com/live?access_key={API_KEY}&currencies={moedas_str}"
        response = requests.get(url)
        data = response.json()

        if data.get("success"):
            cotacoes = data.get("quotes", {})
            timestamp = data.get("timestamp")
        else:
            raise ValueError("Erro ao buscar cotações. Verifique sua chave e plano da API.")

    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Função de conversão de moeda

def converter():
    origem = combo_origem.get()
    destino = "USD"  # Destino fixo
    try:
        valor = float(entrada_valor.get())
    except ValueError:
        resultado_var.set("⚠️ Valor inválido.")
        return

    cot_origem = cotacoes.get(f"USD{origem}")

    if cot_origem is None:
        resultado_var.set("❌ Moeda não suportada.")
        return

    # Conversão: de origem para USD (USD é base)
    valor_convertido = valor / cot_origem
    resultado_var.set(f"{valor:.2f} {origem} = {valor_convertido:.2f} {destino}")

# Interface principal
buscar_cotacoes()

app = tk.Tk()
app.title("Conversor de Moedas Moderno")
app.geometry("600x600")
app.configure(bg="#f0f2f5")

# Seletor de moeda
tk.Label(app, text="Moeda de Origem:", bg="#f0f2f5").pack()
combo_origem = ttk.Combobox(app, values=list(moedas.keys()))
combo_origem.set("BRL")
combo_origem.pack()

# Moeda de destino fixa como USD
tk.Label(app, text="Moeda de Destino (fixa: USD):", bg="#f0f2f5").pack()
tk.Label(app, text="USD", bg="#f0f2f5", font=("Arial", 10, "bold")).pack()

# Valor a converter
tk.Label(app, text="Valor:", bg="#f0f2f5").pack()
entrada_valor = ttk.Entry(app)
entrada_valor.pack()

# Botão de conversão
tk.Button(app, text="Converter", command=converter).pack(pady=10)

# Resultado da conversão
resultado_var = tk.StringVar()
tk.Label(app, textvariable=resultado_var, font=("Arial", 12, "bold"), bg="#f0f2f5").pack()

# Hora da última atualização
if timestamp:
    dt = datetime.fromtimestamp(timestamp)
    tk.Label(app, text=f"🕒 Atualizado em: {dt.strftime('%d/%m/%Y %H:%M:%S')}", bg="#f0f2f5").pack()

# Lista de todas as cotações disponíveis
tk.Label(app, text="\nCotações atuais (base: USD):", bg="#f0f2f5", font=("Arial", 10, "bold")).pack()
frame_lista = tk.Frame(app, bg="#ffffff", relief=tk.SUNKEN, borderwidth=1)
frame_lista.pack(padx=10, pady=5, fill="both", expand=True)

lista_cotacoes = tk.Text(frame_lista, wrap="word", height=20)
lista_cotacoes.pack(expand=True, fill="both")

for cod, nome in moedas.items():
    valor = cotacoes.get(f"USD{cod}", None)
    if valor:
        lista_cotacoes.insert(tk.END, f"1 USD = {valor:.4f} {cod} ({nome})\n")

app.mainloop()