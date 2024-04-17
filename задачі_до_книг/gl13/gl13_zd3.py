#Калькулятор миль на галлон бензина.
from tkinter import *

class Program:
    def __init__(self) -> None:
        self.mw = Tk()
        self.mw.title('Калькулятор')
        self.mw.geometry('500x500+200-200')
        self.mw.resizable(False,False)
        
        self.lab_obem_baku = Label(self.mw,text="Введіть об\'єм баку: ").place(x=10,y=10)
        self.entry_obem_baku = Entry(self.mw)
        self.entry_obem_baku.place(x=120,y=12)
        
        self.lab_kilometr = Label(self.mw,text="Введіть відстань яку проїжає автомобіль: ").place(x=10,y=50)
        self.entry_lab_kilometr = Entry(self.mw)
        self.entry_lab_kilometr.place(x=240,y=52)
        
        self.qiut = Button(self.mw,text='Вийти',width=10,height=2,bg='red',command=self.mw.destroy).place(x=200,y=300)
        self.vuchiclutu = Button(self.mw,text='Обчислити',width=10,height=2,bg='grey',command=self.calculate).place(x=100,y=300)
        
        self.lab_res = Label(self.mw,text='1 л/км: ')
        self.lab_res.place_forget()
        
        self.value = StringVar()
        self.res = Label(self.mw,textvariable=self.value)
        
        mainloop()
        

    def calculate(self):
        self.lab_res.place(x=10,y=90)
        
        kilo = float(self.entry_lab_kilometr.get())
        obem = float(self.entry_obem_baku.get())
        
        self.res.place(x=50,y=90)
        self.value.set(f'{kilo/obem:.2}')
        
        
if __name__=='__main__':
    a = Program()