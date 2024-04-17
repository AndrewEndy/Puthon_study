# Налог на недвижимость.
from tkinter import *

class Program:
    def __init__(self) -> None:
        self.mw = Tk()
        self.mw.title('Обчислювач налога')
        self.mw.geometry('500x500+200-200')
        self.mw.resizable(False,False)
        
        self.lab_cost = Label(self.mw,text='Введіть вартість нерухомості: ').place(x=10,y=10)
        self.entry_cost = Entry(self.mw)
        self.entry_cost.place(x=180,y=10)
        
        self.lab_res = Label(self.mw, text='Податок який потрібно сплатити: ')
        self.lab_res.place_forget()
        
        self.value = StringVar()
        self.res = Label(self.mw,textvariable=self.value)
        
        self.quit = Button(self.mw,text='Вийти', width=10,height=2,bg='red',command=self.mw.destroy).place(x=200,y=100)
        self.calculate = Button(self.mw,text='Обчислити', width=10,height=2,command=self.calculatef).place(x=100,y=100)
        
        mainloop()
        
        
    def calculatef(self):
        self.lab_res.place(x=10,y=50)
        
        cost = float(self.entry_cost.get())
        real_cost = cost * (60/100)
        
        tax_cost=0.75
        while real_cost>100:
            tax_cost+=0.75
            real_cost-=100
        
        self.res.place(x=200,y=50)
        self.value.set(tax_cost)
        
if __name__ == '__main__':
    a = Program()