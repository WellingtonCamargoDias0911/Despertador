# Importação das bibliotecas necessárias
import tkinter as tk
from tkinter import Label, Frame, StringVar, OptionMenu, Button
from datetime import datetime
from time import sleep
from os import system

# Função que verifica o horário atual e dispara o alarme
def alarm():
    while True:  # Laço infinito para verificar o horário a cada segundo
        # Obtém o horário definido pelo usuário (hora, minuto e segundo)
        set_alarm_time = f'{hour.get()}:{minute.get()}:{second.get()}'
        
        sleep(1)  # Pausa de 1 segundo antes de verificar novamente
        # Obtém o horário atual do sistema no formato HH:MM:SS
        current_time = datetime.now().strftime('%H:%M:%S')
        
        # Exibe no terminal o horário atual e o horário definido para o alarme (para debug)
        print(current_time, set_alarm_time)

        # Se o horário atual for igual ao horário definido para o alarme, dispara o alarme
        if current_time == set_alarm_time:
            system('start Alarm.wav')  # Executa o comando para tocar o arquivo de áudio "Alarm.wav"
            break  # Interrompe o laço após disparar o alarme

# Criação da janela principal usando tkinter
root = tk.Tk()
root.geometry('400x200')  # Define o tamanho da janela
root.title('Alarme Pythonico | Programador Aventureiro')  # Define o título da janela

# Criação e exibição do título "Alarme Pythônico" na interface
Label(root, text='Alarme Pythônico', font=('Helvetica 20 bold')).pack(pady=10)
# Criação e exibição do subtítulo "Definir alarme"
Label(root, text='Definir alarme').pack(pady=5)

# Criação de um frame para organizar os widgets na interface
frame = Frame(root)
frame.pack()

# Função para criar um menu suspenso de seleção (OptionMenu) para hora, minuto ou segundo
def option(value):
    opt = StringVar(root)  # Variável que irá armazenar o valor selecionado
    # Cria uma lista de opções com números formatados com dois dígitos (ex: 00, 01, ..., 59)
    options = [str(i).zfill(2) for i in range(value)]
    opt.set(options[0])  # Define o valor padrão da opção como o primeiro da lista
    # Cria o menu suspenso e o adiciona ao frame
    OptionMenu(frame, opt, *options).pack(side=tk.LEFT)
    return opt

# Criação dos menus suspensos para selecionar hora, minuto e segundo
hour = option(24)  # Hora (0-23)
minute = option(60)  # Minuto (0-59)
second = option(60)  # Segundo (0-59)

# Criação do botão "Definir" que chama a função `alarm` quando pressionado
Button(root, text='Definir', font=('Helvetica 15'), command=alarm).pack(pady=20)

# Inicia o loop principal da interface gráfica (aguarda interação do usuário)
root.mainloop()
