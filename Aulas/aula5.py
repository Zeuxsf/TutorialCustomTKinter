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

#Criando frames
frame1 = ctk.CTkFrame(master= janela, width=200 , height=330,fg_color='red',border_color='white', border_width=10).place(x=10,y=60)

frame2 = ctk.CTkFrame(janela,200,330,fg_color='gold',corner_radius=1000).place(x=230, y=60)

frame3 = ctk.CTkFrame(janela,200,330, fg_color='blue',bg_color='white', corner_radius=30).place(x=450,y=60)

janela.mainloop()