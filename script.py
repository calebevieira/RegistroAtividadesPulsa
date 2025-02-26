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
        self.root.geometry("550x750")
        
        # Criando um frame para organizar os campos de entrada
        frame_campos = tk.Frame(root)
        frame_campos.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Nome do Analista (Combobox)
        tk.Label(frame_campos, text="Nome do Analista:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        analistas = ["Wilvan Santos", "Thais Ferreira", "Samuel Amaral", "Nathalia Ponciano", "Luiz Princival", "Kelvin Betto", "Jonatan Atilio", "Gabriel Alves", "Filipe Faria", "Calebe Vieira", "Bruno Altmann"]
        self.nome_analista = ttk.Combobox(frame_campos, values=analistas, state="readonly", width=25)
        self.nome_analista.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Data com calendário
        tk.Label(frame_campos, text="Data:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.data = tk.Entry(frame_campos)
        self.data.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.cal_button = tk.Button(frame_campos, text="Selecionar Data", command=self.abrir_calendario)
        self.cal_button.grid(row=1, column=2, padx=5, pady=5)
        
        # Criando um frame para os checkboxes de sistema
        frame_sistemas = tk.LabelFrame(root, text="Sistemas")
        frame_sistemas.pack(padx=10, pady=5, fill="both")
        
        sistemas_lista = ["Goffice", "Hemote", "Sbs", "Monetários", "Whatsaap", "Teams", "Outlook"]
        self.sistemas = {}
        for i, sistema in enumerate(sistemas_lista):
            var = tk.BooleanVar()
            chk = tk.Checkbutton(frame_sistemas, text=sistema, variable=var)
            chk.grid(row=i // 2, column=i % 2, sticky="w", padx=5, pady=2)
            self.sistemas[sistema] = var
        
        # Primeiro Atendimento (Checkbox Sim/Não)
        frame_primeiro = tk.LabelFrame(root, text="Primeiro Atendimento")
        frame_primeiro.pack(padx=10, pady=5, fill="both")
        self.primeiro_atendimento = tk.StringVar()
        self.primeiro_atendimento.set("Não")
        tk.Radiobutton(frame_primeiro, text="Sim", variable=self.primeiro_atendimento, value="Sim").pack(anchor="w")
        tk.Radiobutton(frame_primeiro, text="Não", variable=self.primeiro_atendimento, value="Não").pack(anchor="w")
        
        # Status (Checkboxes)
        frame_status = tk.LabelFrame(root, text="Status")
        frame_status.pack(padx=10, pady=5, fill="both")
        self.status = {}
        status_lista = ["Concluído", "Atendendo", "Em Andamento"]
        for status in status_lista:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(frame_status, text=status, variable=var)
            chk.pack(anchor="w")
            self.status[status] = var
        
        # Criando um frame para os campos adicionais
        frame_campos_extra = tk.Frame(root)
        frame_campos_extra.pack(padx=10, pady=5, fill="both")
        
        self.campos = ["Número de chamado", "Projeto", "Atividade realizada", "Complemento de informação", "Hora de início", "Hora de término"]
        self.entries = {}
        for i, campo in enumerate(self.campos):
            tk.Label(frame_campos_extra, text=campo + ":").grid(row=i, column=0, sticky="w", padx=5, pady=5)
            self.entries[campo] = tk.Entry(frame_campos_extra)
            self.entries[campo].grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            if "Hora" in campo:
                self.entries[campo].bind("<KeyRelease>", self.formatar_hora)
        
        # Botão de salvar
        btn_salvar = tk.Button(root, text="Salvar Registro", command=self.salvar_registro)
        btn_salvar.pack(pady=10, ipadx=20, ipady=5)
    
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
        # Implementação de salvamento
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroAtividadesApp(root)
    root.mainloop()
