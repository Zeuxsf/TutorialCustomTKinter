
# libraries Import
from tkinter import *
import customtkinter

# Main Window Properties

window = Tk()
window.title("Tkinter")
window.geometry("800x350")
window.configure(bg="#FFFFFF")

Button_id1 = customtkinter.CTkButton(
    master=window,
    text="Aperte",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=30,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Button_id1.place(x=340, y=280)
Entry_id3 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id3.place(x=290, y=200)
Entry_id2 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Placeholder",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=195,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id2.place(x=290, y=160)
Checkbox_id4 = customtkinter.CTkCheckBox(
    master=window,
    text="Checkbox4",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    )
Checkbox_id4.place(x=290, y=240)


#run the main loop
window.mainloop()