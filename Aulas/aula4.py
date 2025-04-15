import customtkinter as ctk

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

#Criando nova janela
def novatela():
    newjanela = ctk.CTkToplevel(janela) 
    newjanela.geometry('300x300')
    btn_newtela = ctk.CTkButton(master=newjanela,text='8080', command= numero)
    btn_newtela.pack()

def numero():
    print('8080')

btn_newtela = ctk.CTkButton(master=janela,text='Abrir janela', command= novatela).place(x= 300, y= 100 ) 
btn_newtela = ctk.CTkButton(master=janela,text='8080', command= numero).place(x= 200, y= 100 ) 


janela.mainloop()