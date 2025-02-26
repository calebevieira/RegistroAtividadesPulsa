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
        
        frame_campos = tk.Frame(root)
        frame_campos.pack(padx=10, pady=10, fill="both", expand=True)
        
        tk.Label(frame_campos, text="Nome do Analista:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        analistas = ["Wilvan Santos", "Thais Ferreira", "Samuel Amaral", "Nathalia Ponciano", "Luiz Princival", "Kelvin Betto", "Jonatan Atilio", "Gabriel Alves", "Filipe Faria", "Calebe Vieira", "Bruno Altmann"]
        self.nome_analista = ttk.Combobox(frame_campos, values=analistas, state="readonly", width=25)
        self.nome_analista.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        tk.Label(frame_campos, text="Data:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.data = tk.Entry(frame_campos)
        self.data.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.cal_button = tk.Button(frame_campos, text="Selecionar Data", command=self.abrir_calendario)
        self.cal_button.grid(row=1, column=2, padx=5, pady=5)
        
        frame_sistemas = tk.LabelFrame(root, text="Sistemas")
        frame_sistemas.pack(padx=10, pady=5, fill="both")
        
        sistemas_lista = ["Goffice", "Hemote", "Sbs", "Monetários", "Whatsaap", "Teams", "Outlook"]
        self.sistemas = {}
        for i, sistema in enumerate(sistemas_lista):
            var = tk.BooleanVar()
            chk = tk.Checkbutton(frame_sistemas, text=sistema, variable=var)
            chk.grid(row=i // 2, column=i % 2, sticky="w", padx=5, pady=2)
            self.sistemas[sistema] = var
        
        frame_primeiro = tk.LabelFrame(root, text="Primeiro Atendimento")
        frame_primeiro.pack(padx=10, pady=5, fill="both")
        self.primeiro_atendimento = tk.StringVar()
        self.primeiro_atendimento.set("Não")
        tk.Radiobutton(frame_primeiro, text="Sim", variable=self.primeiro_atendimento, value="Sim").pack(anchor="w")
        tk.Radiobutton(frame_primeiro, text="Não", variable=self.primeiro_atendimento, value="Não").pack(anchor="w")
        
        frame_status = tk.LabelFrame(root, text="Status")
        frame_status.pack(padx=10, pady=5, fill="both")
        self.status = {}
        status_lista = ["Concluído", "Atendendo", "Em Andamento"]
        for status in status_lista:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(frame_status, text=status, variable=var)
            chk.pack(anchor="w")
            self.status[status] = var
        
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
        arquivo_excel = "registros_atividades.xlsx"
        
        dados = {
            "Nome do Analista": self.nome_analista.get(),
            "Data": self.data.get(),
            "Número de chamado": self.entries["Número de chamado"].get(),
            "Projeto": self.entries["Projeto"].get(),
            "Atividade realizada": self.entries["Atividade realizada"].get(),
            "Complemento de informação": self.entries["Complemento de informação"].get(),
            "Hora de início": self.entries["Hora de início"].get(),
            "Hora de término": self.entries["Hora de término"].get(),
            "Primeiro Atendimento": self.primeiro_atendimento.get(),
            "Status": ", ".join([s for s, var in self.status.items() if var.get()]),
            "Sistemas": ", ".join([s for s, var in self.sistemas.items() if var.get()])
        }
        
        df_novo = pd.DataFrame([dados])
        
        if os.path.exists(arquivo_excel):
            df_existente = pd.read_excel(arquivo_excel)
            df_final = pd.concat([df_existente, df_novo], ignore_index=True)
        else:
            df_final = df_novo
        
        df_final.to_excel(arquivo_excel, index=False)
        
        messagebox.showinfo("Sucesso", "Registro salvo com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroAtividadesApp(root)
    root.mainloop()
