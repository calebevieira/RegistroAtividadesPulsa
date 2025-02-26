import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
import pandas as pd
import os
from datetime import datetime

class RegistroAtividadesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Atividades")
        self.root.geometry("500x600")
        
        self.campos = [
            "Número de chamado", "Sistema", "Primeiro atendimento", "Projeto",
            "Atividade realizada", "Complemento de informação", "Hora de início",
            "Hora de término", "Status"
        ]
        
        self.entries = {}
        
        # Nome do Analista
        tk.Label(root, text="Nome do Analista:").pack()
        self.nome_analista = tk.Entry(root)
        self.nome_analista.pack()
        
        # Data com calendário
        tk.Label(root, text="Data:").pack()
        self.data = tk.Entry(root)
        self.data.pack()
        self.cal_button = tk.Button(root, text="Selecionar Data", command=self.abrir_calendario)
        self.cal_button.pack()
        
        # Campos de entrada
        for campo in self.campos:
            tk.Label(root, text=campo + ":").pack()
            self.entries[campo] = tk.Entry(root)
            self.entries[campo].pack()
            if "Hora" in campo:
                self.entries[campo].bind("<KeyRelease>", self.formatar_hora)
        
        # Botão de salvar
        tk.Button(root, text="Salvar Registro", command=self.salvar_registro).pack(pady=10)
    
    def abrir_calendario(self):
        self.top = tk.Toplevel(self.root)
        self.top.title("Selecionar Data")
        self.cal = Calendar(self.top, date_pattern='dd/MM/yyyy')
        self.cal.pack()
        tk.Button(self.top, text="Selecionar", command=self.definir_data).pack()
    
    def definir_data(self):
        self.data.delete(0, tk.END)
        self.data.insert(0, self.cal.get_date())
        self.top.destroy()
    
    def formatar_hora(self, event):
        widget = event.widget
        texto = widget.get().replace(":", "").replace("/", "")
        if len(texto) > 2:
            texto = texto[:2] + ":" + texto[2:]
        if len(texto) > 5:
            texto = texto[:5]
        widget.delete(0, tk.END)
        widget.insert(0, texto)
    
    def salvar_registro(self):
        dados = {"Nome do Analista": self.nome_analista.get(), "Data": self.data.get()}
        for campo, entry in self.entries.items():
            dados[campo] = entry.get()
        
        arquivo = "Atividades_Diarias.xlsx"
        df_novo = pd.DataFrame([dados])
        
        if os.path.exists(arquivo):
            df_existente = pd.read_excel(arquivo)
            df_final = pd.concat([df_existente, df_novo], ignore_index=True)
        else:
            df_final = df_novo
        
        df_final.to_excel(arquivo, index=False)
        messagebox.showinfo("Sucesso", "Registro salvo com sucesso!")
        self.limpar_campos()
        
    def limpar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.nome_analista.delete(0, tk.END)
        self.nome_analista.insert(0, "")
        self.data.delete(0, tk.END)
        self.data.insert(0, datetime.today().strftime('%d/%m/%Y'))

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroAtividadesApp(root)
    root.mainloop()