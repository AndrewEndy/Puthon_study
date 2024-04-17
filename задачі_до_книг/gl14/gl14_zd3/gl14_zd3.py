#Проект реляционной базы данных
import tkinter as t
from tkinter import font
from tkinter import messagebox 
import sqlite3 as sql

class Program:
    def __init__(self) -> None:
        
        self.__specialty = 'спеціальність'
        self.__facultie = 'факультет'
        
        self.create_main_sql()
        self.create_main_tkinter()
        
        t.mainloop()
        
# Головні функції --->
    def create_main_tkinter(self):
        self.mw = t.Tk()
        self.mw.title('Students')
        self.mw.geometry('800x700+400+100')
        self.mw.resizable(False,False)
        
        self.custom_font = font.Font(family="Helvetica", size=14, weight="bold")
        
        self.operation_info = t.Label(self.mw, text='Операції',font=self.custom_font)
        self.operation_info.place(x=95,y=10)
        
        self.listbox = t.Listbox(self.mw, width=40)
        self.listbox.place(x=20,y=40)
        self.first_filling_of_the_listbox()
        
        self.quit = t.Button(self.mw, text='Вийти', bg='red', width=10, height=2,command=self.mw.destroy).place(x=300,y=500)
        
        self.gl_button = t.Button(self.mw, text='Вибрати', width=10, height=2,command=self.distributor)
        self.gl_button.place(x=200,y=500)
        
        
    def create_main_sql(self):
        self.__URL = 'gl14/gl14_zd3/student_info.db'
        self.con = sql.connect(self.__URL)
        self.cur = self.con.cursor()
        self.cur.execute( 'PRAGMA foreign_keys=ON')
        
        self.cur.execute('CREATE TABLE IF NOT EXISTS Majors(MajorsID INTEGER PRIMARY KEY NOT NULL, Name TEXT)')
        
        self.cur.execute('CREATE TABLE IF NOT EXISTS Departments(DepartmentsID INTEGER PRIMARY KEY NOT NULL, Name TEXT)')
        
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Students(StudentsID INTEGER PRIMARY KEY NOT NULL, Name TEXT, MajorsID INTEGER, DepartmentsID INTEGER,
                         FOREIGN KEY(MajorsID) REFERENCES Majors(MajorsID), FOREIGN KEY(DepartmentsID) REFERENCES Departments(DepartmentsID) )''')
        
        self.con.commit()
        self.con.close()    
        
        
    def first_filling_of_the_listbox(self):
        self.listbox.delete(0, t.END) 
        
        self.listbox.insert(0, 'Студенти')
        self.listbox.insert(1, 'Спеціальності')
        self.listbox.insert(2, 'Факультети')
        self.listbox.select_set(0)
# <---
        
# Розприділітель
    def distributor(self, value='---'):
        if value == '': pass 
        else:
            index = self.listbox.curselection()
            value = self.listbox.get(index)
        
        if value == 'Студенти': self.student_distributor()
        if value == 'Спеціальності': self.specialty_distributor()
        if value == 'Факультети': self.facultie_distributor()
        
        if value == 'Назад': self.first_filling_of_the_listbox()
        
        if value == 'Додати нового студента': self.add_new_studet()
        if value == 'Вивести інформацію про студентів': self.show_students()
        if value == 'Відшукати студента': self.find_student()
        if value == 'Змінити інформацію студента': self.change_information_about_student()
        if value == 'Видалити студента': self.delete_student()
        
        if value == 'Додати нову спеціальність':self.create_new_object(name=self.__specialty)
        if value == 'Відшукати спеціальність': self.find_object(name=self.__specialty)
        if value == 'Змінити спеціальність': self.update_object(name=self.__specialty)
        if value == 'Видалити спеціальність': self.delete_object(name=self.__specialty)
        if value == 'Вивести існуючі спеціальності': self.show_specialty()
        
        if value == 'Додати новий факультет': self.create_new_object(name=self.__facultie)
        if value == 'Відшукати факультет': self.find_object(name=self.__facultie)
        if value == 'Змінити факультет': self.update_object(name=self.__facultie)
        if value == 'Видалити факультет': self.delete_object(name=self.__facultie)
        if value == 'Вивести існуючі факультети': self.show_facultie()
        
# Показати функції студента
    def student_distributor(self):
        self.listbox.delete(0, t.END) 
        
        self.listbox.insert(0, 'Додати нового студента')
        self.listbox.insert(1, 'Відшукати студента')
        self.listbox.insert(2, 'Змінити інформацію студента')
        self.listbox.insert(3, 'Видалити студента')
        self.listbox.insert(4, 'Вивести інформацію про студентів')
        self.listbox.insert(5, 'Назад')
        self.listbox.select_set(4)
        self.distributor(value='')
    
    
# Показати функції среціальності    
    def specialty_distributor(self):
        self.listbox.delete(0, t.END) 
        
        self.listbox.insert(0, 'Додати нову спеціальність')
        self.listbox.insert(1, 'Відшукати спеціальність')
        self.listbox.insert(2, 'Змінити спеціальність')
        self.listbox.insert(3, 'Видалити спеціальність')
        self.listbox.insert(4, 'Вивести існуючі спеціальності')
        self.listbox.insert(5, 'Назад')
        self.listbox.select_set(4)
        self.distributor(value='')


# Показати функції Факультета    
    def facultie_distributor(self):
        self.listbox.delete(0, t.END) 
        
        self.listbox.insert(0, 'Додати новий факультет')
        self.listbox.insert(1, 'Відшукати факультет')
        self.listbox.insert(2, 'Змінити факультет')
        self.listbox.insert(3, 'Видалити факультет')
        self.listbox.insert(4, 'Вивести існуючі факультети')
        self.listbox.insert(5, 'Назад')
        self.listbox.select_set(4)
        self.distributor(value='')
    

# Спільні функції --->
    def on_button_click(self):
        self.running = False
        
        
    def create_new_object(self, name):
        self.listbox.place_forget()
        self.operation_info.place_forget()
        self.gl_button.place_forget()
        
        temp_button = t.Button(self.mw,text='Додати', width=10, height=2,command=self.on_button_click)
        temp_button.place(x=200,y=500)
        
        temp_lab1 = t.Label(self.mw, text=f'Введіть назву: ')
        temp_lab1.place(x=20,y=50)
        temp_lab2 = t.Label(self.mw, text=f'Введіть ID: ')
        temp_lab2.place(x=20,y=90)
        temp_lab3 = t.Label(self.mw, text=f'Додати нову {name}', font=self.custom_font)
        temp_lab3.place(x=10,y=10)

        temp_entry_name = t.Entry(self.mw,width=50)
        temp_entry_name.place(x=180, y=52)
        temp_entry_id = t.Entry(self.mw,width=6)
        temp_entry_id.place(x=160, y=92)
        
        self.running=True
        while self.running:
            self.mw.update()
            
        id = int(temp_entry_id.get())
        name_obj = str(temp_entry_name.get())
        
        self.con = sql.connect(self.__URL)
        self.cur = self.con.cursor()
        
        if name==self.__specialty:
            self.cur.execute('''SELECT MajorsID FROM Majors WHERE MajorsID==?''', (id,))
            if self.cur.fetchall() != []:
                messagebox.showinfo('Помилка', 'Дане ID зайняте!')
        elif name==self.__facultie:
            self.cur.execute('''SELECT DepartmentsID FROM Departments WHERE DepartmentsID==?''', (id,))
            if self.cur.fetchall() != []:
                messagebox.showinfo('Помилка', 'Дане ID зайняте!')
        else:
            if name == self.__specialty:
                self.cur.execute('''INSERT INTO Majors(MajorsID, Name) VALUES(?, ?)''', (id, name_obj))
            if name == self.__facultie:
                self.cur.execute('''INSERT INTO Departments(DepartmentsID, Name) VALUES(?, ?)''', (id, name_obj))
        
        self.con.commit()
        self.con.close()
        
        temp_button.destroy()
        temp_entry_id.destroy()
        temp_entry_name.destroy()
        temp_lab1.destroy()
        temp_lab2.destroy()
        temp_lab3.destroy()
        
        self.listbox.place(x=20,y=40)
        self.operation_info.place(x=95,y=10)
        self.gl_button.place(x=200,y=500)
        self.first_filling_of_the_listbox()
        
            
    def find_object(self, name):
        
        self.listbox.place_forget()
        self.operation_info.place_forget()
        self.gl_button.place_forget()
        
        temp_button = t.Button(self.mw, text='Вибрати', width=10, height=2, command=self.on_button_click)
        temp_button.place(x=200,y=500)
        
        temp_title_lab = t.Label(self.mw, text=f'Знайти {name}', font=self.custom_font)
        temp_title_lab.place(x=10,y=10)
        
        # Шукати ПО --->
        temp_find_lab = t.Label(self.mw,text='Шукати по: ',font='Arial 12')
        temp_find_lab.place(x=10,y=50)
        
        choice_var = t.IntVar()
        rb1 = t.Radiobutton(self.mw, text='ID',font='Arial 12', variable=choice_var, value=1)
        rb1.place(x=100, y=50)
        
        rb2 = t.Radiobutton(self.mw, text='Назві',font='Arial 12', variable=choice_var, value=2)
        rb2.place(x=160, y=50)
        # <---
        
        self.running=True
        while self.running:
            self.mw.update()
            
            
        choice = choice_var.get()

        rb1.destroy()
        rb2.destroy()
        
        temp_button.config(text='Знайти')
        
        temp_entry = t.Entry(self.mw, width=6)
        temp_entry.place(x=100,y=53)
        
        if choice==1:
            temp_find_lab.config(text='Введіть ID: ')
        if choice==2:
            temp_find_lab.config(text='Введіть назву: ')
            temp_entry.place(x=130,y=53)
            temp_entry.config(width=12)
        
        
        self.running=True
        while self.running:
            self.mw.update()
        
        
        self.con = sql.connect(self.__URL)
        self.cur = self.con.cursor()
        
        if choice==1:
            id = int(temp_entry.get())
            
            if name == self.__specialty:
                self.cur.execute('''SELECT MajorsID, Name FROM Majors WHERE MajorsID==?''',(id,))
            if name== self.__facultie:
                self.cur.execute('''SELECT DepartmentsID, Name FROM Departments WHERE DepartmentsID==?''',(id,))
            
        if choice==2:
            name_obj = str(temp_entry.get())
            
            if name == self.__specialty:
                self.cur.execute('''SELECT MajorsID, Name FROM Majors WHERE Name==?''',(name_obj,))
            if name == self.__facultie:
                self.cur.execute('''SELECT DepartmentsID, Name FROM Departments WHERE Name==?''',(name_obj,))
            
        res = self.cur.fetchall()
        
        if res == []:
            messagebox.showinfo('Знайти об\'єкт', f'{name.capitalize()} немає!')
        else:
            str_res=''
            for el in res:
                str_res += f'ID: {el[0]} | Назва: {el[1]}\n'
                 #print(f'ID: {el[0]} | Назва: {el[1]}\n')
            messagebox.showinfo('Всі спеціальності',str_res)
            
        self.con.commit()
        self.con.close()
        
        
        temp_entry.destroy()
        temp_find_lab.destroy()
        temp_button.destroy()
        temp_title_lab.destroy()
        
        
        self.listbox.place(x=20,y=40)
        self.operation_info.place(x=95,y=10)
        self.gl_button.place(x=200,y=500)
        self.first_filling_of_the_listbox()
        
      
    def update_object(self, name):
        self.listbox.place_forget()
        self.operation_info.place_forget()
        self.gl_button.place_forget()
        
        temp_title_lab = t.Label(self.mw, text=f'Змінити {name}', font=self.custom_font)
        temp_title_lab.place(x=10,y=10)
        
        temp_button = t.Button(self.mw, text='Знайти', width=10,height=2, command=self.on_button_click)
        temp_button.place(x=200,y=500)
        
        temp_lab = t.Label(self.mw, text='Введіть ID: ', font='Arial 12')
        temp_lab.place(x=10,y=50)
        
        temp_entry1 = t.Entry(self.mw, width=6)
        temp_entry1.place(x=100, y=53)
        
        self.running=True
        while self.running:
            self.mw.update()
            
        temp_button.config(text='Змінити')
            
        id = int(temp_entry1.get())
        
        self.con = sql.connect(self.__URL)
        self.cur = self.con.cursor()
        
        if name==self.__specialty:
            self.cur.execute('''SELECT MajorsID FROM Majors WHERE MajorsID==?''', (id,))
            if self.cur.fetchall() == []:
                messagebox.showinfo('Помилка', 'Даної спеціальності немає!')
        elif name==self.__facultie:
            self.cur.execute('''SELECT DepartmentsID FROM Departments WHERE DepartmentsID==?''', (id,))
            if self.cur.fetchall() == []:
                messagebox.showinfo('Помилка', 'Даного факультету немає!')
        else:
            if name==self.__specialty:
                self.cur.execute('''SELECT MajorsID FROM Majors WHERE MajorsID==?''', (id,))
            if name==self.__facultie:
                self.cur.execute('''SELECT DepartmentsID FROM Departments WHERE DepartmentsID==?''', (id,))
                
            temp = self.cur.fetchall()
            
            if temp==[]:
                messagebox.showinfo(f'Змінити {name}', f'{name} немає!!!')
            else:
                temp_lab.config(text='Введіть нові: ')
                
                temp_lab_id = t.Label(self.mw, text='ID', font='Arial 12')
                temp_lab_id.place(x=110, y=50)
                temp_lab_name = t.Label(self.mw, text='Назва', font='Arial 12')
                temp_lab_name.place(x=210, y=50)
                
                temp_entry1.place(x=135,y=53)
                
                temp_entry2 = t.Entry(self.mw, width=30)
                temp_entry2.place(x=265,y=53)
            
            self.running=True
            while self.running:
                self.mw.update()
            
            id = int(temp_entry1.get())
            name_obj = str(temp_entry2.get())
            
            if name==self.__specialty:
                    self.cur.execute('''UPDATE Majors 
                                        SET MajorsID = ?, 
                                        Name = ? 
                                        WHERE MajorsID == ?''',(id,name_obj,id) )
                    
            if name==self.__facultie:
                    self.cur.execute('''UPDATE Departments 
                                        SET DepartmentsID = ?,
                                        Name = ? 
                                        WHERE DepartmentsID == ?''',(id,name_obj,id) )
            temp_lab_id.destroy()
            temp_lab_name.destroy()
            temp_entry2.destroy()
        
        self.con.commit()
        self.con.close()
        
        
        temp_lab.destroy()
        temp_entry1.destroy()
        temp_button.destroy()
        temp_title_lab.destroy()
        
        self.listbox.place(x=20,y=40)
        self.operation_info.place(x=95,y=10)
        self.gl_button.place(x=200,y=500)
        self.first_filling_of_the_listbox()
        
        
    def delete_object(self, name):
        self.listbox.place_forget()
        self.operation_info.place_forget()
        self.gl_button.place_forget()
        
        temp_title_lab = t.Label(self.mw, text=f'Видалити {name}', font=self.custom_font)
        temp_title_lab.place(x=10,y=10)
        
        temp_button = t.Button(self.mw, text='Видалити', width=10,height=2, command=self.on_button_click)
        temp_button.place(x=200,y=500)
        
        temp_lab = t.Label(self.mw, text='Введіть ID: ', font='Arial 12')
        temp_lab.place(x=10,y=50)
        
        temp_entry1 = t.Entry(self.mw, width=6)
        temp_entry1.place(x=100, y=53)
        
        self.running=True
        while self.running:
            self.mw.update()
            
        id = int(temp_entry1.get())
        
        self.con = sql.connect(self.__URL)
        self.cur = self.con.cursor()
            
        if name==self.__specialty:
            self.cur.execute('''SELECT MajorsID FROM Majors WHERE MajorsID==?''', (id,))
            if self.cur.fetchall() == []:
                messagebox.showinfo('Помилка', 'Даної спеціальності немає!')
        elif name==self.__facultie:
            self.cur.execute('''SELECT DepartmentsID FROM Departments WHERE DepartmentsID==?''', (id,))
            if self.cur.fetchall() == []:
                messagebox.showinfo('Помилка', 'Даного факультету немає!')
        else:
            if name==self.__specialty:
                self.cur.execute('''SELECT MajorsID FROM Majors WHERE MajorsID==?''', (id,))
            if name==self.__facultie:
                self.cur.execute('''SELECT DepartmentsID FROM Departments WHERE DepartmentsID==?''', (id,))
                
            temp = self.cur.fetchall()
            
            if temp==[]:
                messagebox.showinfo(f'Змінити {name}', f'{name} немає!!!')
            else:
                if name==self.__specialty:
                    self.cur.execute('''DELETE FROM Majors WHERE MajorsID == ? ''',(id,))
                if name==self.__facultie:
                    self.cur.execute('''DELETE FROM Departments WHERE DepartmentsID == ? ''',(id,))
            
        self.con.commit()
        self.con.close()
        
        temp_lab.destroy()
        temp_entry1.destroy()
        temp_button.destroy()
        temp_title_lab.destroy()
        
        self.listbox.place(x=20,y=40)
        self.operation_info.place(x=95,y=10)
        self.gl_button.place(x=200,y=500)
        self.first_filling_of_the_listbox()
# <---        
        
# Функції Спеціальності
    def show_specialty(self):
        self.con = sql.connect(self.__URL)
        self.cur = self.con.cursor()
        
        self.cur.execute('''SELECT * FROM Majors ''')
        res = self.cur.fetchall()
        
        if res == []:
            messagebox.showinfo('Всі спеціальності','Пусто')
        else:
            str_res=''
            for el in res:
                str_res += f'ID: {el[0]} | Назва: {el[1]}\n'
                #print(f'ID: {el[0]} | Назва: {el[1]}\n')
            messagebox.showinfo('Всі спеціальності',str_res)
        
        self.con.commit()
        self.con.close()
        
# Функції Факультета     
    def show_facultie(self):
        self.con = sql.connect(self.__URL)
        self.cur = self.con.cursor()
        
        self.cur.execute('''SELECT * FROM Departments ''')
        res = self.cur.fetchall()
        
        if res == []:
            messagebox.showinfo('Всі факультети','Пусто')
        else:
            str_res=''
            for el in res:
                str_res += f'ID: {el[0]} | Назва: {el[1]}\n'
                #print(f'ID: {el[0]} | Назва: {el[1]}\n')
            messagebox.showinfo('Всі факультети',str_res)
        
        self.con.commit()
        self.con.close()
    
# Функції студента --->
    def show_students(self):
        self.con = sql.connect(self.__URL)
        self.cur = self.con.cursor()
        
        self.cur.execute('''SELECT Students.StudentsID,
                                    Students.Name,
                                    Majors.Name,
                                    Departments.Name
                            FROM Students, Majors, Departments
                            WHERE Students.MajorsID == Majors.MajorsID AND
                                Students.DepartmentsID == Departments.DepartmentsID''')
        
        res = self.cur.fetchall()
        
        if res == []:
            messagebox.showinfo('Всі Студенти','Пусто')
        else:
            str_res=''
            for el in res:
                str_res += f'ID: {el[0]} | Ім\'я: {el[1]} | Спеціальність: {el[2]} | Факультет: {el[3]}\n'
                #print(f'ID: {el[0]} | Назва: {el[1]}\n')
            messagebox.showinfo('Всі Студенти',str_res)
        
        self.con.commit()
        self.con.close()
    
    
    def add_new_studet(self):
        self.listbox.place_forget()
        self.operation_info.place_forget()
        self.gl_button.place_forget()
        
        temp_title_lab = t.Label(self.mw, text=f'Додати нового студента', font=self.custom_font)
        temp_title_lab.place(x=10,y=10)

        temp_button = t.Button(self.mw,text='Додати', width=10, height=2,command=self.on_button_click)
        temp_button.place(x=200,y=500)
        
        temp_lab1 = t.Label(self.mw, text=f'Введіть ім\'я: ')
        temp_lab1.place(x=20,y=50)
        
        temp_lab2 = t.Label(self.mw, text=f'Введіть ID: ')
        temp_lab2.place(x=20,y=90)
        
        temp_lab3 = t.Label(self.mw, text=f'Введіть назву спеціальності: ')
        temp_lab3.place(x=20,y=130)
        
        temp_lab4 = t.Label(self.mw, text=f'Введіть назву факультета: ')
        temp_lab4.place(x=20,y=170)
        

        temp_entry_name = t.Entry(self.mw,width=50)
        temp_entry_name.place(x=90, y=52)
        
        temp_entry_id = t.Entry(self.mw,width=6)
        temp_entry_id.place(x=80, y=92)
        
        temp_entry_name_of_specialty = t.Entry(self.mw,width=50)
        temp_entry_name_of_specialty.place(x=180, y=132)
        
        temp_entry_name_of_faculty = t.Entry(self.mw,width=50)
        temp_entry_name_of_faculty.place(x=170, y=172)
        
        self.running=True
        while self.running:
            self.mw.update()
            
        id_st = int(temp_entry_id.get())
        name_st = str(temp_entry_name.get())
        name_of_specailty = str(temp_entry_name_of_specialty.get())
        name_of_faculty = str(temp_entry_name_of_faculty.get())
        
        self.con = sql.connect(self.__URL)
        self.cur = self.con.cursor()
        
        self.cur.execute('''SELECT StudentsID FROM Students WHERE StudentsID==?''',(id_st,))
        temp_res1 = self.cur.fetchall()
        self.cur.execute('''SELECT Name FROM Majors WHERE Name==?''',(name_of_specailty,))
        temp_res2 =self.cur.fetchall()
        self.cur.execute('''SELECT Name FROM Departments WHERE Name==?''',(name_of_faculty,))
        temp_res3 = self.cur.fetchall()
        
        if temp_res1 != []:
            messagebox.showinfo('Помилка', 'Дане ID зайняте!')
        elif temp_res2 == []:
            messagebox.showinfo('Помилка', 'Даної спеціальності немає!')
        elif temp_res3 == []:
            messagebox.showinfo('Помилка', 'Даного факультета немає!')
        else:
            self.cur.execute(''' SELECT DepartmentsID FROM Departments WHERE Name==?''',(name_of_faculty,))
            res = self.cur.fetchall()
            id_faculti = res[0][0]
            
            self.cur.execute(''' SELECT MajorsID FROM Majors WHERE Name==?''',(name_of_specailty,))
            res = self.cur.fetchall()
            id_specialty = res[0][0]
            
            self.cur.execute('''INSERT INTO Students(StudentsID, Name, MajorsID, DepartmentsID) 
                             VALUES(?, ?, ?, ?)''', (id_st, name_st, id_specialty, id_faculti))
        
        self.con.commit()
        self.con.close()
        
        temp_button.destroy()
        temp_entry_id.destroy()
        temp_entry_name.destroy()
        temp_lab1.destroy()
        temp_lab2.destroy()
        temp_lab3.destroy()
        temp_lab4.destroy()
        temp_title_lab.destroy()
        temp_entry_name_of_specialty.destroy()
        temp_entry_name_of_faculty.destroy()
        
        self.listbox.place(x=20,y=40)
        self.operation_info.place(x=95,y=10)
        self.gl_button.place(x=200,y=500)
        self.first_filling_of_the_listbox()
    
    
    def find_student(self):
        self.listbox.place_forget()
        self.operation_info.place_forget()
        self.gl_button.place_forget()
        
        temp_title_lab = t.Label(self.mw, text=f'Знайти студента', font=self.custom_font)
        temp_title_lab.place(x=10,y=10)

        temp_button = t.Button(self.mw,text='Знайти', width=10, height=2,command=self.on_button_click)
        temp_button.place(x=200,y=500)
        
        temp_find_lab = t.Label(self.mw,text='Шукати за: ',font='Arial 12')
        temp_find_lab.place(x=10,y=50)
        
        rb_var = t.IntVar()
        rb_var.set(1)
        
        r1 = t.Radiobutton(self.mw, variable=rb_var, value=1, text='ID', font='Arial 12')
        r1.place(x=100,y=50)
        r2 = t.Radiobutton(self.mw, variable=rb_var, value=2, text='Ім\'ям', font='Arial 12')
        r2.place(x=150,y=50)
        r3 = t.Radiobutton(self.mw, variable=rb_var, value=3, text='Спеціальністю', font='Arial 12')
        r3.place(x=220,y=50)
        r4 = t.Radiobutton(self.mw, variable=rb_var, value=4, text='Факультетом', font='Arial 12')
        r4.place(x=360,y=50)

        self.running=True
        while self.running:
            self.mw.update()
            
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        
        self.con = sql.connect(self.__URL)
        self.cur = self.con.cursor()
        
        temp_entry = t.Entry(self.mw)
            
        if rb_var.get()==1:
            temp_find_lab.config(text='Введіть ID студента: ')
            
            temp_entry.config(width=6)
            temp_entry.place(x=170, y=55)
            
            self.running=True
            while self.running:
                self.mw.update()
                
            if str(temp_entry.get()) == '':
                messagebox.showinfo('Помилка', 'Ви нічого не ввели або ввели некоректні дані!')
                
            id_student = int(temp_entry.get())
            
            self.cur.execute('''SELECT Students.StudentsID,
                                        Students.Name,
                                        Majors.Name,
                                        Departments.Name
                                FROM Students, Majors, Departments
                                WHERE Students.StudentsID==? AND
                                    Students.MajorsID == Majors.MajorsID AND
                                    Students.DepartmentsID == Departments.DepartmentsID''', (id_student,))
            
        if rb_var.get()==2:
            temp_find_lab.config(text='Введіть Ім\'я студента: ')
            
            temp_entry.config(width=50)
            temp_entry.place(x=180, y=55)
            
            self.running=True
            while self.running:
                self.mw.update()
            
            if str(temp_entry.get()) == '':
                messagebox.showinfo('Помилка', 'Ви нічого не ввели або ввели некоректні дані!')
                
            name_student = str(temp_entry.get())
            
            self.cur.execute('''SELECT Students.StudentsID,
                                        Students.Name,
                                        Majors.Name,
                                        Departments.Name
                                FROM Students, Majors, Departments
                                WHERE Students.Name==? AND
                                    Students.MajorsID == Majors.MajorsID AND
                                    Students.DepartmentsID == Departments.DepartmentsID''', (name_student,))
                
        if rb_var.get()==3:
            temp_find_lab.config(text='Введіть спеціальність: ')
            
            temp_entry.config(width=50)
            temp_entry.place(x=180, y=55)
            
            self.running=True
            while self.running:
                self.mw.update()
            
            if str(temp_entry.get()) == '':
                messagebox.showinfo('Помилка', 'Ви нічого не ввели або ввели некоректні дані!')
                
            name_specialty = str(temp_entry.get())
            
            self.cur.execute('''SELECT MajorsID FROM Majors WHERE Name==?''',(name_specialty,))
            if self.cur.fetchall() == []:
                messagebox.showinfo('Помилка', 'Даної спеціальності немає!')
            else:
                self.cur.execute('''SELECT Students.StudentsID,
                                        Students.Name,
                                        Majors.Name,
                                        Departments.Name
                                FROM Students, Majors, Departments
                                WHERE Majors.Name == ? AND
                                    Students.MajorsID == Majors.MajorsID AND
                                    Students.DepartmentsID == Departments.DepartmentsID''', (name_specialty,))
            
        if rb_var.get()==4:
            temp_find_lab.config(text='Введіть факультет: ')
            
            temp_entry.config(width=50)
            temp_entry.place(x=180, y=55)
            
            self.running=True
            while self.running:
                self.mw.update()
            
            if str(temp_entry.get()) == '':
                messagebox.showinfo('Помилка', 'Ви нічого не ввели або ввели некоректні дані!')
                
            name_faculty = str(temp_entry.get())
            
            self.cur.execute('''SELECT DepartmentsID FROM Departments WHERE Name==?''',(name_faculty,))
            if self.cur.fetchall() == []:
                messagebox.showinfo('Помилка', 'Даної спеціальності немає!')
            else:
                self.cur.execute('''SELECT Students.StudentsID,
                                        Students.Name,
                                        Majors.Name,
                                        Departments.Name
                                FROM Students, Majors, Departments
                                WHERE Departments.Name == ? AND
                                    Students.MajorsID == Majors.MajorsID AND
                                    Students.DepartmentsID == Departments.DepartmentsID''', (name_faculty,))
                
        res = self.cur.fetchall()
        
        str_res=''
        for el in res:
            str_res += f'ID: {el[0]} | Ім\'я: {el[1]} | Спеціальність: {el[2]} | Факультет: {el[3]}\n'
        messagebox.showinfo('Всі Студенти',str_res)
        
        self.con.commit()
        self.con.close()
        
        temp_find_lab.destroy()
        temp_entry.destroy()
        temp_button.destroy()
        temp_title_lab.destroy()
        
        
        self.listbox.place(x=20,y=40)
        self.operation_info.place(x=95,y=10)
        self.gl_button.place(x=200,y=500)
        self.first_filling_of_the_listbox()
    
    
    def change_information_about_student(self):
        self.listbox.place_forget()
        self.operation_info.place_forget()
        self.gl_button.place_forget()
        
        temp_title_lab = t.Label(self.mw, text=f'Змінити інформацію про студента', font=self.custom_font)
        temp_title_lab.place(x=10,y=10)

        temp_button = t.Button(self.mw,text='Знайти', width=10, height=2,command=self.on_button_click)
        temp_button.place(x=200,y=500)
        
        
        temp_lab = t.Label(self.mw, text='Введіть ID студента: ', font='Arial 12')
        temp_lab.place(x=10,y=50)
        
        temp_entry = t.Entry(self.mw, width=6)
        temp_entry.place(x=165, y=53)
        
        
        self.running=True
        while self.running:
            self.mw.update()
        
        flagID = int(temp_entry.get())
        
        if str(temp_entry.get()) == '':
                messagebox.showinfo('Помилка', 'Ви нічого не ввели або ввели некоректні дані!')
            
        id_student = int(temp_entry.get())
        
        self.con = sql.connect(self.__URL)
        self.cur = self.con.cursor()
            
        self.cur.execute('''SELECT  StudentsID FROM Students WHERE StudentsID == ?''',(id_student,))
        if self.cur.fetchall == []:
            messagebox.showinfo('Помилка', 'Даного студента немає!')
        else:
            temp_lab.config(text='Введіть нові данні студента: ')
            temp_button.config(text='Змінити')
            
            e1_stVar = t.StringVar()
            e2_stVar = t.StringVar()
            e3_stVar = t.StringVar()
            e4_stVar = t.StringVar()
            
            temp_lab0 = t.Label(self.mw, text='ID', font='Arial 12')
            temp_lab0.place(x=220, y=50)
            temp_entry.place(x=245, y=53)
            temp_entry.config(textvariable=e1_stVar)
            
            temp_lab1 = t.Label(self.mw, text='Ім\'я', font='Arial 12')
            temp_lab1.place(x=280, y=50)
            temp_entry1 = t.Entry(self.mw, width=50, textvariable=e2_stVar)
            temp_entry1.place(x=320,y=53)
            
            temp_lab2 = t.Label(self.mw, text='Спеціальність', font='Arial 12')
            temp_lab2.place(x=10, y=100)
            temp_entry2 = t.Entry(self.mw, width=20, textvariable=e3_stVar)
            temp_entry2.place(x=120,y=103)
            
            temp_lab3 = t.Label(self.mw, text='Факультет', font='Arial 12')
            temp_lab3.place(x=270, y=100)
            temp_entry3 = t.Entry(self.mw, width=40, textvariable=e4_stVar)
            temp_entry3.place(x=365,y=103)
            
            self.cur.execute('''SELECT StudentsID, Name, MajorsID, DepartmentsID FROM Students WHERE StudentsID==?''', (id_student,))
            res = self.cur.fetchall()
            
            e1_stVar.set(res[0][0])
            e2_stVar.set(res[0][1])
            
            self.cur.execute('''SELECT Name FROM Majors WHERE MajorsID==?''', (res[0][2],))
            res1 = self.cur.fetchall()
            e3_stVar.set(res1[0][0])
            
            self.cur.execute('''SELECT Name FROM Departments WHERE DepartmentsID==?''', (res[0][3],))
            res1 = self.cur.fetchall()
            e4_stVar.set(res1[0][0])
            
            self.running=True
            while self.running:
                self.mw.update()
            
            if str(temp_entry.get()) == '' or str(temp_entry1.get()) == '' or str(temp_entry2.get()) == '' or str(temp_entry3.get()) == '':
                messagebox.showinfo('Помилка','Ви нічого не ввели або ввели некоректні дані!')
                
            id_student = int(temp_entry.get())
            name_student = str(temp_entry1.get())
            specialty = str(temp_entry2.get())
            faculty = str(temp_entry3.get())
            
            self.cur.execute('''SELECT Name FROM Majors WHERE Name==?''',(specialty,))
            temp_res2 =self.cur.fetchall()
            self.cur.execute('''SELECT Name FROM Departments WHERE Name==?''',(faculty,))
            temp_res3 = self.cur.fetchall()
            
            if flagID != id_student:
                self.cur.execute('''SELECT StudentsID FROM Students WHERE StudentsID==?''',(id_student,))
                if self.cur.fetchall() != []:
                    messagebox.showinfo('Помилка', 'Дане ID зайняте')
                
            if temp_res2 == []:
                messagebox.showinfo('Помилка', 'Даної спеціальності немає!')
            elif temp_res3 == []:
                messagebox.showinfo('Помилка', 'Даного факультета немає!')
            else:
                self.cur.execute('''SELECT MajorsID FROM Majors WHERE Name==?''', (specialty,))
                res1 = self.cur.fetchall()
                id_specialty = res1[0][0]
                
                self.cur.execute('''SELECT DepartmentsID FROM Departments WHERE Name==?''', (faculty,))
                res1 = self.cur.fetchall()
                id_faculty = res1[0][0]
                
                self.cur.execute('''UPDATE Students
                                    SET Name = ?,
                                    MajorsID = ?,
                                    DepartmentsID = ?
                                    WHERE StudentsID == ?''',( name_student, id_specialty, id_faculty, flagID))
                
                self.cur.execute('''UPDATE Students
                                    SET StudentsID = ?
                                    WHERE Name == ?''',( id_student,name_student))
        
        self.con.commit()
        self.con.close()
        
        temp_entry1.destroy()
        temp_entry2.destroy()
        temp_entry3.destroy()
        temp_lab0.destroy()
        temp_lab1.destroy()
        temp_lab2.destroy()
        temp_lab3.destroy()
        temp_entry.destroy()
        temp_lab.destroy()
        temp_button.destroy()
        temp_title_lab.destroy()

        
        self.listbox.place(x=20,y=40)
        self.operation_info.place(x=95,y=10)
        self.gl_button.place(x=200,y=500)
        self.first_filling_of_the_listbox()
        
        
    def delete_student(self):
        self.listbox.place_forget()
        self.operation_info.place_forget()
        self.gl_button.place_forget()
        
        temp_title_lab = t.Label(self.mw, text=f'Видалити студента', font=self.custom_font)
        temp_title_lab.place(x=10,y=10)

        temp_button = t.Button(self.mw,text='Видалити', width=10, height=2,command=self.on_button_click)
        temp_button.place(x=200,y=500)
        
        
        temp_lab = t.Label(self.mw, text='Введіть ID студента: ', font='Arial 12')
        temp_lab.place(x=10,y=50)
        
        temp_entry = t.Entry(self.mw, width=6)
        temp_entry.place(x=165, y=53)
        
        self.running=True
        while self.running:
            self.mw.update()
            
        id_st = int(temp_entry.get())
        
        self.con = sql.connect(self.__URL)
        self.cur = self.con.cursor()
            
        self.cur.execute('''SELECT StudentsID From Students WHERE StudentsID==? ''',(id_st,))
        if self.cur.fetchall() == []:
            messagebox.showinfo('Помилка', 'Даного студента немає!')
        else:
            self.cur.execute(''' DELETE FROM Students WHERE StudentsID == ?''',(id_st,))
            
            
        self.con.commit()
        self.con.close()
        
        temp_entry.destroy()
        temp_lab.destroy()
        temp_button.destroy()
        temp_title_lab.destroy()

        
        self.listbox.place(x=20,y=40)
        self.operation_info.place(x=95,y=10)
        self.gl_button.place(x=200,y=500)
        self.first_filling_of_the_listbox()
# --->        
        
        
if __name__=='__main__':
    a = Program()