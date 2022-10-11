from tkinter import *
from tkinter import messagebox 
import customtkinter
from kasse import *
import datetime as dt
import pandas as pd
import numpy as np
from PIL import ImageTk, Image

kasse = Kasse()

root = customtkinter.CTk()

root.title('Cash System')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
root.geometry("1000x500")
root.configure(bg='black')


def kosten_anzeigen():
   quantity = (int(bier_combobox.get()),0,int(shots_combobox.get()),int(longdrink_combobox.get()))
   kosten = kasse.kalkuriere_kosten(quantity)
   costs_entry.configure(text=f'{kosten}')
   rueckgeld_entry.configure(text='')
   return kosten
   
def shortcut_kosten():
   if shortcut_kosten_entry.get() == 'Leave this entry':
      messagebox.showwarning("Warning", "Don't press this button!")
   else:
      try:
         kasse.kassenstand += int(shortcut_kosten_entry.get())   
         kassenbestand_label.configure(text=f'Cash Balance: {kasse.kassenstand}')
         with open('C:/Users/paulg/Documents/Coding/GUI/Zeiterfassung/kassenstand.txt', 'w+') as f:
            f.write(str(kasse.kassenstand))
         shortcut_kosten_entry.delete(0, 'end')
         shortcut_kosten_entry.insert(0, 'Leave this entry')   
      except:
         messagebox.showerror('Fatal Error', 'Something went wrong!')
         shortcut_kosten_entry.delete(0, 'end')
         shortcut_kosten_entry.insert(0, 'Leave this entry')
      
      
def finish_order():
   kosten = kosten_anzeigen()
   if kosten != 0 and erloes_entry.get() != '':
      erloes = int(erloes_entry.get())
      rueckgeld = kasse.getränke_verkauf(erloes, kosten)
      rueckgeld_entry.configure(text=f'{rueckgeld}')
      kasse.kassenstand += erloes - rueckgeld
      kassenbestand_label.configure(text=f'Cash Balance: {kasse.kassenstand}')
      
      costs_entry.configure(text='')
      erloes_entry.delete(0, 'end')
      
      with open('C:/Users/paulg/Documents/Coding/GUI/Zeiterfassung/kassenlog.csv', 'a+') as f:
         f.write(f'{erloes},{kosten},{erloes-kosten},{kasse.kassenstand},{int(shots_combobox.get())},{int(bier_combobox.get())},{int(longdrink_combobox.get())},{check_happy_hour()}\n')
      with open('C:/Users/paulg/Documents/Coding/GUI/Zeiterfassung/kassenstand.txt', 'w+') as f:
         f.write(str(kasse.kassenstand))
            
      shots_combobox.set('0')
      bier_combobox.set('0')
      longdrink_combobox.set('0')   
   else:
      messagebox.showerror('Information missing', 'Please fill out income and costs!')
      
       
      
 
      
frame = customtkinter.CTkFrame(master=root,
                               width=1000,
                               height=500,
                               corner_radius=10,
                               bg='black',
                               fg_color='black',
                               border_width=2, border_color="white")





kosten_label = customtkinter.CTkLabel(root, text="Quick Income:", width=130,
                               height=40,
                               fg_color=("#e76f51", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black')

shortcut_kosten_entry = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                              fg_color='#e76f51',
                              fg='white',
                              text_font=('Times New Roman', 24),
                              justify=CENTER,
                              bg_color='black',
                              border_width=2, border_color="white",
                              text_color='black'
                            )

shortcut_kosten_button = customtkinter.CTkButton(root, width=195,
                                 height=30,
                                 corner_radius=8,
                                 command=shortcut_kosten,
                                 text="Press only under stress",
                                 fg_color='#e76f51',
                                 text_font=('Times New Roman', 24),
                               bg_color='black',
                               hover_color='#3AB4F2',
                               border_width=2, border_color="white",
                               text_color='black'
                                 )







getraenke_label = customtkinter.CTkLabel(root, text="Drink:", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )

menge_label = customtkinter.CTkLabel(root, text="Quantity:", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )

kassenbestand_label = customtkinter.CTkLabel(root, text=f"Cash Balance: {kasse.kassenstand}", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )





img = ImageTk.PhotoImage(Image.open("C:/Users/paulg/Documents/Coding/GUI/Zeiterfassung/party.jpg"))
img_label = customtkinter.CTkLabel(master=root, image=img)





shots_label = customtkinter.CTkLabel(root, text="Shots:", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )
shots_combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=[f"{i}" for i in range(20)], 
                                       width=80,
                                        height=40,
                                        fg_color=("#2a9d8f", "#0F3D3E"),
                                        corner_radius=8, 
                                        text_font=('Times New Roman', 24),
                                        bg_color='black',
                                        text_color='black',
                                        
                                        button_color='#0F3D3E',
                                        button_hover_color='#3AB4F2',
                                        dropdown_text_font=('Times New Roman', 24),
                                                           
                                        )










bier_label = customtkinter.CTkLabel(root, text="Beer/Wine:", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )
bier_combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=[f"{i}" for i in range(20)], 
                                       width=80,
                                        height=40,
                                        fg_color=("#2a9d8f", "#0F3D3E"),
                                        corner_radius=8, 
                                        text_font=('Times New Roman', 24),
                                        bg_color='black',
                                        text_color='black',
                                        
                                        button_color='#0F3D3E',
                                        button_hover_color='#3AB4F2',
                                        dropdown_text_font=('Times New Roman', 24),
                                                           
                                        )








longdrink_label = customtkinter.CTkLabel(root, text="Longdrink:", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )
longdrink_combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=[f"{i}" for i in range(20)], 
                                       width=80,
                                        height=40,
                                        fg_color=("#2a9d8f", "#0F3D3E"),
                                        corner_radius=8, 
                                        text_font=('Times New Roman', 24),
                                        bg_color='black',
                                        text_color='black',
                                        
                                        button_color='#0F3D3E',
                                        button_hover_color='#3AB4F2',
                                        dropdown_text_font=('Times New Roman', 24),
                                                           
                                        )







calc_cost_button = customtkinter.CTkButton(root, width=195,
                                 height=40,
                                 corner_radius=8,
                                 command=kosten_anzeigen,
                                 text="Calculate costs",
                                 fg_color='#2a9d8f',
                                 text_font=('Times New Roman', 24),
                               bg_color='black',
                               hover_color='#3AB4F2',
                               border_width=2, border_color="white",
                               text_color='black'
                                 )







erloes_label = customtkinter.CTkLabel(root, text="Income:", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )

costs_label = customtkinter.CTkLabel(root, text="Costs:", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )

rueckgeld_label = customtkinter.CTkLabel(root, text="Change:", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )








erloes_entry = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                              fg_color='#2a9d8f',
                              fg='white',
                              text_font=('Times New Roman', 20),
                              justify=CENTER,
                              bg_color='black',
                              border_width=2, border_color="white",
                              text_color='black'
                            )
costs_entry = customtkinter.CTkLabel(root, text="", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )

rueckgeld_entry = customtkinter.CTkLabel(root, text="", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )






finish_order_button = customtkinter.CTkButton(root, width=195,
                                 height=40,
                                 corner_radius=8,
                                 command=finish_order,
                                 text="Finish order",
                                 fg_color='#2a9d8f',
                                 text_font=('Times New Roman', 24),
                               bg_color='black',
                               hover_color='#3AB4F2',
                               border_width=2, border_color="white",
                               text_color='black'
                                 )



#Packing them on the screen
frame.grid(row=0, column=0, columnspan=6, rowspan=10, sticky='news')

kosten_label.grid(row=0, column=0, columnspan=2, rowspan=1, sticky='ew', padx=10)
shortcut_kosten_entry.grid(row=0, column=2, sticky='ew', padx=10, columnspan=2)
shortcut_kosten_entry.insert(0, 'Leave this entry')
shortcut_kosten_button.grid(row=0, column=4, sticky='ew', padx=10, columnspan=2)

getraenke_label.grid(row=1, column=0, columnspan=2, rowspan=1, sticky='ew', padx=10)
menge_label.grid(row=1, column=2, columnspan=2, rowspan=1, sticky='ew', padx=10)
kassenbestand_label.grid(row=1, column=4, columnspan=2, rowspan=1, sticky='ew', padx=10)

img_label.grid(row=2, column=4, columnspan=2, rowspan=3, padx=10, pady=10, sticky='nsew')


shots_label.grid(row=2, column=0, columnspan=2, rowspan=1, sticky='ew', padx=10)
shots_combobox.grid(row=2, column=2, columnspan=2, rowspan=1, sticky='ew', padx=10)
shots_combobox.set('0')


bier_label.grid(row=3, column=0, columnspan=2, rowspan=1, sticky='ew', padx=10)
bier_combobox.grid(row=3, column=2, columnspan=2, rowspan=1, sticky='ew', padx=10)
bier_combobox.set('0')


longdrink_label.grid(row=4, column=0, columnspan=2, rowspan=1, sticky='ew', padx=10)
longdrink_combobox.grid(row=4, column=2, columnspan=2, rowspan=1, sticky='ew', padx=10)
longdrink_combobox.set('0')

calc_cost_button.grid(row=5, column=0, columnspan=6, sticky='ew', padx=10)


erloes_label.grid(row=6, column=0, columnspan=2, sticky='ew', padx=10)
costs_label.grid(row=6, column=2, columnspan=2, sticky='ew', padx=10)
rueckgeld_label.grid(row=6, column=4, columnspan=2, sticky='ew', padx=10)
   
   
erloes_entry.grid(row=7, column=0, columnspan=2, sticky='ew', padx=10)   
costs_entry.grid(row=7, column=2, columnspan=2, sticky='ew', padx=10)  
rueckgeld_entry.grid(row=7, column=4, columnspan=2, sticky='ew', padx=10)   


finish_order_button.grid(row=8, column=0, columnspan=6, sticky='ew', padx=10)

root.mainloop()