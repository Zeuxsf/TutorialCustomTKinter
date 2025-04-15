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

#Label - Print do ctk
ctk.CTkLabel(janela,text='Galinhas Voadoras', width=100,height=100).pack()

#Introduzindo label por input e entry

#Entry
def enviar():
    print(entry.get())
    label.configure(text=str(entry.get()))
    pass

#Quando for uma informação que vai ser recebida na hora, o '.pack()' tem que vir separadamente, não pode ficar na mesma linha
label = ctk.CTkLabel(janela,100,20,text='',text_color='gold')
label.pack()

entry = ctk.CTkEntry(janela,100,20)
entry.pack()

btn = ctk.CTkButton(janela,10,10,text='Clique aqui',command=enviar).pack()

#Input
#texto = str(input('Digite um texto: '))

#ctk.CTkLabel(janela,text=texto).pack()


janela.mainloop()