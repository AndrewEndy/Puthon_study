#Переводчик с латинского
import tkinter

class Transletor:
    def __init__(self) -> None:
        self.mw = tkinter.Tk()
        self.mw.title('Перекладач')
        self.mw.geometry('500x500+200-200')
        
        self.lab_latin = tkinter.Label(self.mw, text='Латинська',width=10,height=2,bg='grey').place(x=10,y=10)
        
        self.lab_rus = tkinter.Label(self.mw, text='руска',width=10,height=2,bg='grey').place(x=300,y=10)
        
        self.latin_frame = tkinter.Frame(self.mw)
        self.latin1 = tkinter.Label(self.latin_frame, text='sinister',width=10,height=2,bg='grey').pack()
        self.latin2 = tkinter.Label(self.latin_frame, text='dexter',width=10,height=2,bg='grey').pack()
        self.latin3 = tkinter.Label(self.latin_frame, text='medium',width=10,height=2,bg='grey').pack()
        self.latin_frame.place(x=10,y=70)
        
        self.button_frame = tkinter.Frame(self.mw)
        self.button1 = tkinter.Button(self.button_frame,text='Перекласти',width=10,height=2,bg='red',command=self.translate1).pack()
        self.button2 = tkinter.Button(self.button_frame,text='Перекласти',width=10,height=2,bg='red',command=self.translate2).pack()
        self.button3 = tkinter.Button(self.button_frame,text='Перекласти',width=10,height=2,bg='red',command=self.translate3).pack()
        self.button_frame.place(x=150,y=60)
        
        self.rus_frame = tkinter.Frame(self.mw)
        self.rus1 = tkinter.Label(self.rus_frame, text='Левый',width=10,height=2,bg='grey')
        self.rus1.pack_forget()
        self.rus2 = tkinter.Label(self.rus_frame, text='Правый',width=10,height=2,bg='grey')
        self.rus2.pack_forget()
        self.rus3 = tkinter.Label(self.rus_frame, text='Центральный',width=10,height=2,bg='grey')
        self.rus3.pack_forget()
        self.rus_frame.place(x=300,y=70)
        
        self.quit = tkinter.Button(self.mw, text='Вийти',width=10,height=2,bg='blue',command=self.mw.destroy).place(x=150,y=200)
        
        tkinter.mainloop()
        
    def translate1(self):
        self.rus1.pack()
    
    def translate2(self):
        self.rus2.pack()

    def translate3(self):
        self.rus3.pack()




if __name__=='__main__':
    a = Transletor()