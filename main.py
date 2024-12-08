import tkinter as tk
from tkinter import messagebox
from pyswip import Prolog

# Inicializar Prolog
prolog = Prolog()

# Carregar o arquivo Prolog
prolog.consult("sistema_sangue.pl") 

# Funções de consulta
def consultar_aptos_para_receptor():
    receptor = entry_name.get()
    if not receptor:
        messagebox.showerror("Erro", "Insira o nome de um receptor.")
        return
    
    query = f"podeDoar(X, {receptor})."
    resultados = list(prolog.query(query))
    
    if resultados:
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"Quem pode doar para {receptor}:\n")
        for res in resultados:
            resultado_text.insert(tk.END, f"- {res['X']}\n")
    else:
        messagebox.showinfo("Sem resultados", f"Ninguém pode doar para {receptor}.")

def consultar_para_quem_pode_doar():
    doador = entry_name.get()
    if not doador:
        messagebox.showerror("Erro", "Insira o nome de um doador.")
        return
    
    query = f"podeDoar({doador}, X)."
    resultados = list(prolog.query(query))
    
    if resultados:
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"Para quem {doador} pode doar:\n")
        for res in resultados:
            resultado_text.insert(tk.END, f"- {res['X']}\n")
    else:
        messagebox.showinfo("Sem resultados", f"{doador} não pode doar para ninguém.")

def consultar_por_tipo_sanguineo():
    tipo = entry_name.get()
    if not tipo:
        messagebox.showerror("Erro", "Insira um tipo sanguíneo.")
        return
    
    query = f"tiposanguineo(X, {tipo})."
    resultados = list(prolog.query(query))
    
    if resultados:
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"Pessoas com tipo sanguíneo {tipo}:\n")
        for res in resultados:
            resultado_text.insert(tk.END, f"- {res['X']}\n")
    else:
        messagebox.showinfo("Sem resultados", f"Ninguém possui tipo sanguíneo {tipo}.")

def consultar_por_fator_rh():
    fator_rh = entry_name.get()
    if not fator_rh:
        messagebox.showerror("Erro", "Insira um fator Rh (+ ou -).")
        return
    
    query = f"fatorrh(X, '{fator_rh}')."
    resultados = list(prolog.query(query))
    
    if resultados:
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"Pessoas com fator Rh {fator_rh}:\n")
        for res in resultados:
            resultado_text.insert(tk.END, f"- {res['X']}\n")
    else:
        messagebox.showinfo("Sem resultados", f"Ninguém possui fator Rh {fator_rh}.")

# Configuração da interface
root = tk.Tk()
root.title("Sistema Especialista de Doação de Sangue")

# Entrada de nome ou tipo
frame_input = tk.Frame(root)
frame_input.pack(pady=10)
tk.Label(frame_input, text="Entrada (nome, tipo ou fator Rh):").pack(side=tk.LEFT, padx=5)
entry_name = tk.Entry(frame_input)
entry_name.pack(side=tk.LEFT, padx=5)

# Botões de consulta
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_receptor = tk.Button(frame_buttons, text="Quem pode doar para", command=consultar_aptos_para_receptor)
btn_receptor.pack(side=tk.LEFT, padx=5)

btn_doador = tk.Button(frame_buttons, text="Para quem pode doar", command=consultar_para_quem_pode_doar)
btn_doador.pack(side=tk.LEFT, padx=5)

btn_tipo = tk.Button(frame_buttons, text="Pessoas com tipo sanguíneo", command=consultar_por_tipo_sanguineo)
btn_tipo.pack(side=tk.LEFT, padx=5)

btn_rh = tk.Button(frame_buttons, text="Pessoas com fator Rh", command=consultar_por_fator_rh)
btn_rh.pack(side=tk.LEFT, padx=5)

# Área de resultados
resultado_text = tk.Text(root, height=15, width=50)
resultado_text.pack(pady=10)

# Rodar a interface
root.mainloop()
