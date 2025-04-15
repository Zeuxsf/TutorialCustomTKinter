import customtkinter as ctk
import tkinter
from time import sleep
from PIL import Image


img = ctk.CTkImage(light_image=Image.open("./neo.png"),dark_image=(Image.open("./neo.png")),size=(50,50))

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
ctk.CTkLabel(janela,text='Galinhas Voadoras. Aula 14', width=100,height=100).pack()

#Slider - Barra de slide

def valor(value):
    print(value)
    pass

slider = ctk.CTkSlider(janela,from_=0,to=100,command=valor)
slider.pack()


janela.mainloop()