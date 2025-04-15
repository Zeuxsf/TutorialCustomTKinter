import customtkinter as ctk
from time import sleep

janela = ctk.CTk()

#Define o nome da janela
janela.title('Tutorial-Custom-Tkinter')

#Define o tamanho inicial da janela
janela.geometry('700x400')

#Define o tamanho max da janela
janela.maxsize(width=900, height=550)

#Define o tamanho mínimo da janela
janela.minsize(width=700, height=400)

#Permite ou não a janela ser redimensionável (mantém o tamanho fixo caso os dois sejam false)
janela.resizable(width=False, height=False)

#Define o tema 
janela._set_appearance_mode('dark') #Existem apenas dark, light e system (é interessante colocar o 'system' para o programa se adequar ao computador do usuário)

#Option Menu
ctk.CTkLabel(janela,text='Menu de Opções', font=('arial bold', 20)).pack(pady = 20, padx = 20)

ctk.CTkLabel(janela,text='Sua Idade: ', font=('arial bold', 15)).place(x=10, y= 70)

#É a mesma coisa que o optmenu.set
mes_var = ctk.StringVar(value='Escolha sua Idade')

def idade(escolha):
    print(f'Sua idade é: {escolha}')

optmenu = ctk.CTkOptionMenu(janela,values=['18', '19', '20', '21'], command=idade, variable=mes_var)
optmenu.place(x= 10, y= 130)

#
#def mes(escolha):
#    print(f'O seu mês de nascimento é: {escolha}')
#
#optmenu = ctk.CTkOptionMenu(janela,values=['Abril', 'Maio', 'Junho', 'Julho'], command=mes)
#optmenu.set('Mês de escolha')
#optmenu.place(x= 10, y= 100)


janela.mainloop()