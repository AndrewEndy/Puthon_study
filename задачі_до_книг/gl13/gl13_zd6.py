#Авторемонтная фирма "Автоцех"
from tkinter import *

class Program:
    def __init__(self) -> None:
        self.mw = Tk()
        self.mw.title('Обчислювач налога')
        self.mw.geometry('500x500+200-200')
        self.mw.resizable(False,False)
        
        self.info = Label(self.mw, text='Послуги СТО \"Автоцех\"').place(x=150,y=10)
        
        self.create()
        
        self.quit = Button(self.mw,text='Вийти', width=10,height=2,bg='red',command=self.mw.destroy).place(x=200,y=400)
        self.calculate = Button(self.mw,text='Обчислити', width=10,height=2,command=self.calculatef).place(x=100,y=400)
        
        self.res_info = Label(self.mw,text='До сплати: ')
        self.res_info.place_forget()
        
        self.value = StringVar()
        self.res = Label(self.mw, textvariable=self.value)
        
        mainloop()
        
        
    def calculatef(self):
        self.res_info.place(x=100,y=310)
        self.res.place(x=170,y=310)
        self.value.set(self.ifs())
        
    
    
    def create(self):
        self.frame = Frame(self.mw)
        
        self.ch_var1 = IntVar()
        self.ch_var2 = IntVar()
        self.ch_var3 = IntVar()
        self.ch_var4 = IntVar()
        self.ch_var5 = IntVar()
        self.ch_var6 = IntVar()
        self.ch_var7 = IntVar()
        
        self.ch_var1.set(0)
        self.ch_var2.set(0)
        self.ch_var3.set(0)
        self.ch_var4.set(0)
        self.ch_var5.set(0)
        self.ch_var6.set(0)
        self.ch_var7.set(0)
        
        self.ch1 = Checkbutton(self.frame,text='заміна масла — 500.00 грн', variable=self.ch_var1)
        self.ch2 = Checkbutton(self.frame,text='смазочні роботи — 300.00 грн', variable=self.ch_var2)
        self.ch3 = Checkbutton(self.frame,text='промивка радіатора — 700.00 грн', variable=self.ch_var3)
        self.ch4 = Checkbutton(self.frame,text='заміна жидкості в трансмісії — 1000.00 грн', variable=self.ch_var4)
        self.ch5 = Checkbutton(self.frame,text='провірка — 800.00 грн', variable=self.ch_var5)
        self.ch6 = Checkbutton(self.frame,text='заміна глушителя вихлопа — 1300.00 грн', variable=self.ch_var6)
        self.ch7 = Checkbutton(self.frame,text='заміна шин — 1300.00 грн', variable=self.ch_var7)
        
        self.ch1.pack(padx=5,pady=5)
        self.ch2.pack(padx=5,pady=5)
        self.ch3.pack(padx=5,pady=5)
        self.ch4.pack(padx=5,pady=5)
        self.ch5.pack(padx=5,pady=5)
        self.ch6.pack(padx=5,pady=5)
        self.ch7.pack(padx=5,pady=5)
        
        self.frame.place(x=100,y=50)


    def ifs(self):
        sum=0
        if self.ch_var1.get()==1:
            sum+=500
        if self.ch_var2.get()==1:
            sum+=300
        if self.ch_var3.get()==1:
            sum+=700
        if self.ch_var4.get()==1:
            sum+=1000
        if self.ch_var5.get()==1:
            sum+=800
        if self.ch_var6.get()==1:
            sum+=1300
        if self.ch_var7.get()==1:
            sum+=1300
        return sum
    
    
if __name__=='__main__':
    a = Program()