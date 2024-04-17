# Из шкалы Цельсия в шкалу Фаренгейта
from tkinter import *

class Program:
    def __init__(self) -> None:
        self.mw = Tk()
        self.mw.title('Конвертор')
        self.mw.geometry('500x500+200-200')
        self.mw.resizable(False,False)
        
        self.lab_C = Label(self.mw,text='Введіть градуси по Цельсію: ').place(x=10,y=10)
        self.entry_C = Entry(self.mw,width=5)
        self.entry_C.place(x=170,y=10)
        
        self.lab_F = Label(self.mw,text='Градуси Цельсія по шкалі Фаренгейта: ')
        self.lab_F.place_forget()
        
        self.value = StringVar()
        self.res_F = Label(self.mw,textvariable=self.value)
        
        self.quit = Button(self.mw,text='Вийти', width=10,height=2,bg='red',command=self.mw.destroy).place(x=200,y=100)
        self.calculate = Button(self.mw,text='Обчислити', width=10,height=2,command=self.calculatef).place(x=100,y=100)
        mainloop()
        
        
    def calculatef(self):
        self.lab_F.place(x=10,y=50)
        
        celcii = float(self.entry_C.get())
        self.res_F.place(x=200,y=50)
        
        res=9/5*celcii+32
        self.value.set(f'{res:.2f}')

        
if __name__=='__main__':
    a = Program()
