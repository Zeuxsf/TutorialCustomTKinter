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

#Caixa de Dialogo (Dialog)

def abrir():
    dialog = ctk.CTkInputDialog(title='num',text='número de cell',entry_text_color='gold')
    num = int(dialog.get_input())
    if num == 5:
        print('Funciona1')
    else:
        print('sexo')    

btn = ctk.CTkButton(janela, text='Abrir caixa de diálogo', command=abrir)
btn.pack()

janela.mainloop()