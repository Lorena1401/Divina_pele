import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar

janela = tk.Tk()
janela.configure(bg='light blue')
janela.title("Divina Pele - Agendamento")
janela.geometry("400x500")

def salvar_agendamento(nome, telefone, data, hora, servico):
    with open("agendamentos.txt", "a", encoding="utf-8") as f:
        f.write(f"Nome: {nome}\nTelefone: {telefone}\nData: {data}\nHora: {hora}\nServiço: {servico}\n")
        f.write("-" * 30 + "\n")

class AgendamentoApp:
    def __init__(janela, root):
        janela.root = root
        janela.root.configure(bg="#00BFFF")
        janela.nome = ""
        janela.telefone = ""
        janela.servico = ""
        janela.horario = ""
        janela.tela_boas_vindas()

    def limpar_tela(janela):
        for widget in janela.root.winfo_children():
            widget.destroy()

    def tela_boas_vindas(janela):
        janela.limpar_tela()
        tk.Label(janela.root, text="Bem-vindo(a) à Divina Pele ", font=("Arial", 14, "bold"), bg="#87CEFA").pack(pady=30)
        tk.Button(janela.root, text="Começar Agendamento", command=janela.tela_login, bg="#87CEFA", font=("Arial", 12)).pack(pady=10)

    def tela_login(janela):
        janela.limpar_tela()
        tk.Label(janela.root, text="Informe seus dados:", font=("Arial", 13), bg="#00BFFF").pack(pady=10)

        tk.Label(janela.root, text="Seu nome:", bg="#00BFFF").pack()
        nome_entry = tk.Entry(janela.root)
        nome_entry.pack()

        tk.Label(janela.root, text="Seu telefone:", bg="#00BFFF").pack()
        telefone_entry = tk.Entry(janela.root)
        telefone_entry.pack()

        def proximo():
            janela.nome = nome_entry.get()
            janela.telefone = telefone_entry.get()
            if not janela.nome or not janela.telefone:
                messagebox.showerror("Ops!", "Por favor, preencha seu nome e telefone.")
                return
            janela.tela_calendario()

        tk.Button(janela.root, text="Avançar", command=proximo, bg="#00BFFF", font=("Arial", 12)).pack(pady=20)

    def tela_calendario(janela):
        janela.limpar_tela()
        tk.Label(janela.root, text="Escolha a data do atendimento:", font=("Arial", 12), bg="#00BFFF").pack(pady=5)
        janela.cal = Calendar(janela.root, selectmode='day')
        janela.cal.pack(pady=10)

        def proximo():
            janela.data_selecionada = janela.cal.get_date()
            janela.tela_servico()

        tk.Button(janela.root, text="Próximo", command=proximo, bg="#00BFFF", font=("Arial", 12)).pack(pady=20)

    def tela_servico(janela):
        janela.limpar_tela()
        tk.Label(janela.root, text="Qual serviço você deseja?", font=("Arial", 12), bg="#00BFFF").pack(pady=5)
        servicos = ["Máscaras faciais", "Penteados", "Maquiagens", "Rejuvenescimento", "Aromaterapia", "Massagens", "Limpeza de Pele"]
        servico_combobox = ttk.Combobox(janela.root, values=servicos)
        servico_combobox.pack(pady=10)

        def proximo():
            janela.servico = servico_combobox.get()
            if not janela.servico:
                messagebox.showerror("Erro", "Selecione um serviço.")
                return
            janela.tela_horario()

        tk.Button(janela.root, text="Próximo ", command=proximo, bg="#00BFFF", font=("Arial", 12)).pack(pady=20)

    def tela_horario(janela):
        janela.limpar_tela()
        tk.Label(janela.root, text="Escolha o horário ideal:", font=("Arial", 12), bg="#00BFFF").pack(pady=5)
        horarios = ["09:00", "10:00", "12:00", "14:00", "15:00", "16:00", "17:00"]
        horario_combobox = ttk.Combobox(janela.root, values=horarios)
        horario_combobox.pack(pady=10)

        def agendar():
            janela.horario = horario_combobox.get()
            salvar_agendamento(janela.nome, janela.telefone, janela.data_selecionada, janela.horario, janela.servico)
            messagebox.showinfo("Agendamento Confirmado", f"Olá {janela.nome}!\nSeu atendimento foi marcado para {janela.data_selecionada} às {janela.horario}.\nServiço: {janela.servico}")
            janela.root.destroy()

        tk.Button(janela.root, text="Confirmar Agendamento ", command=agendar, bg="#00BFFF", font=("Arial", 12)).pack(pady=20)

AgendamentoApp(janela)
janela.mainloop()