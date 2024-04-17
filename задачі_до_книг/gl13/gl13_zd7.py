# Междугородные звонки
from tkinter import *
class Program:
    def __init__(self) -> None:
        self.mw = Tk()
        self.mw.title('Міжнародні звінки')
        self.mw.geometry('500x500+200-200')
        self.mw.resizable(False,False)
        
        self.create_main()
        self.info_res = Label(self.mw,text='До сплати: ')
        
        self.value = StringVar()
        self.res = Label(self.mw, textvariable=self.value)
        
        self.calculate_b = Button(self.mw, text='Обчислити', command=self.calculate)
        self.calculate_b.place(x=100,y=400)
        self.quit = Button(self.mw, text = 'Вийти', bg='red', command=self.mw.destroy)
        self.quit.place(x=200,y=400)
        
        mainloop()
        
        
    def create_main(self):
        self.info1 = Label(self.mw, text='Категорії тарифа').place(x=10,y=10)
        self.info2 = Label(self.mw, text='Тариф хв/грн').place(x=200,y=10)
        
        self.info11 = Label(self.mw, text='Дений час(з 6:00 до 17:59)').place(x=10,y=50)
        self.info21 = Label(self.mw, text='10').place(x=225,y=50)
        
        self.info12 = Label(self.mw, text='Вечірній час(з 18:00 до 23:59)').place(x=10,y=90)
        self.info22 = Label(self.mw, text='12').place(x=225,y=90)
        
        self.info13 = Label(self.mw, text='Не піковий період(з 24:00 до 5:59)').place(x=10,y=130)
        self.info23 = Label(self.mw, text='5').place(x=225,y=130)
        
        self.radio_var = IntVar()
        
        self.rd1 = Radiobutton(self.mw, text = 'Вибрати', variable=self.radio_var, value=1)
        self.rd2 = Radiobutton(self.mw, text = 'Вибрати', variable=self.radio_var, value=2)
        self.rd3 = Radiobutton(self.mw, text = 'Вибрати', variable=self.radio_var, value=3)
        self.rd1.place(x=275,y=50)
        self.rd2.place(x=275,y=90)
        self.rd3.place(x=275,y=130)
        
        self.ent_lab = Label(self.mw, text='Введіть час: ').place(x=100, y=180)
        self.entry = Entry(self.mw)
        self.entry.place(x=180,y=180)
        
        
    def calculate(self):
        time = float(self.entry.get())
        self.info_res.place(x=100,y=250)
        self.res.place(x=160,y=250)
        
        sum=0
        if self.radio_var.get()==1:
            sum = time*10
        if self.radio_var.get()==2:
            sum = time*12
        if self.radio_var.get()==3:
            sum = time*5
            
        self.value.set(sum)
        
        
if __name__=='__main__':
    a = Program()