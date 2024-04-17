# ФИО и адрес
import tkinter


class Program:
    def __init__(self) -> None:
        self.mw = tkinter.Tk()
        self.mw.title('Інформація')
        
        self.top_frame = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)
        
        self.value = tkinter.StringVar()
        self.res_label= tkinter.Label(self.top_frame,textvariable=self.value)
        
        self.button_info = tkinter.Button(self.bottom_frame,text='Показати інфо',command=self.show_info)
        self.button_quit = tkinter.Button(self.bottom_frame,text='Вийти',command=self.mw.destroy)
        
        self.res_label.pack(side='top')
        self.button_info.pack(side='left')
        self.button_quit.pack(side='right')
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
        
    def show_info(self):
        self.value.set(f'Україна\nм.Чернівці\nвул.Чорноморська 13\nПастух Андрій Юрійович')
        
        tkinter.mainloop()


if __name__=='__main__':
    obj = Program()