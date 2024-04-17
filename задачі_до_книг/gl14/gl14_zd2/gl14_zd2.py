#Телефонная база данных

import sqlite3

class Telephon_program:
    def __init__(self) -> None:
        self.__URL = 'gl14/gl14_zd2/phonebook.db'
        self.con = sqlite3.connect(self.__URL)
        self.cur = self.con.cursor()
        
        self.cur.execute('CREATE TABLE IF NOT EXISTS Entries(id INTEGER PRIMARY KEY NOT NULL, Name TEXT, PhoneNumber INTEGER)')
        
        self.con.commit()
        self.con.close()
        
        self.menu()
        
    
    def menu(self):
        while True:
            print('---MENU---')
            print('1.Додати новий контакт')
            print('2.Знайти контакт')
            print('3.Змінити контакт')
            print('4.Видалити контакт')
            print('5.Переглянути контакти')
            print('6.Вихід')
            choice = int(input('Ваш вибір: '))
            
            if choice==1: self.Add_contact()
            if choice==2: self.Find_Contact()
            if choice==3: self.Change_Contact()
            if choice==4: self.Delete_Contact()
            if choice==5: self.View_Contacts()
            if choice==6: break
            
        
    def Add_contact(self):
        print()
        self.con = sqlite3.connect(self.__URL)
        self.cur = self.con.cursor()
        
        name = str(input('Введіть ваше імя: '))
        phone_number = int(input('Введіть ваш номер телефона: '))
        
        print('Додаєм...')
        self.cur.execute('INSERT INTO Entries(Name, PhoneNumber) VALUES(?,?)',(name,phone_number))
        print('Успішно добавлено!')
        self.con.commit()
        self.con.close()
        print()
        
        
    def Find_Contact(self):
        print()
        self.con = sqlite3.connect(self.__URL)
        self.cur = self.con.cursor()
        
        print('Шукати по...')
        print('1.ID')
        print('2.Назві')
        print('3.Номеру телефона')
        choice = int(input('Вибір: '))
        
        if choice==1:
            id = int(input('Введіть ID: '))
            self.cur.execute('''SELECT id, Name, PhoneNumber FROM Entries WHERE id == ?''',(id,))
            
        if choice==2:
            name = str(input('Введіть імя: '))
            self.cur.execute('SELECT id, Name, PhoneNumber FROM Entries WHERE Name == ?',(name,))
        
        if choice==3:
            phnm = int(input('Введіть номер телефону: '))
            self.cur.execute('''SELECT id, Name, PhoneNumber FROM Entries WHERE PhoneNumber == ?''',(phnm,))
        
        res = self.cur.fetchall()
        
        if res==[]: print('\n---Даного контакту немає АБО данні введені неправильно---\n')
        else:
            print(f'ID:{res[0][0]} | Name: {res[0][1]} | Phone number: {res[0][2]}\n')
            
        self.con.commit()
        self.con.close()
        print()


    def Change_Contact(self):
        print()
        self.con = sqlite3.connect(self.__URL)
        self.cur = self.con.cursor()
        
        id = int(input('Введіть ID контакта, який хочете змінити: '))
        self.cur.execute('''SELECT id, Name, PhoneNumber FROM Entries WHERE id == ?''',(id,))
        res = self.cur.fetchall()
        
        if res==[]: print('\n---Даного контакту немає АБО данні введені неправильно---\n')
        
        else:
            print('Введіть нові данні: ')
            name = str(input('Імя: '))
            phnm = int(input('Номер: '))
            
            print('Змінюєм...')
            self.cur.execute('''UPDATE Entries
                                SET Name = ?,
                                PhoneNumber = ?
                                WHERE id == ?''',(name,phnm,id))
            print('Зміни успішно встановлені!')
        
        self.con.commit()
        self.con.close()
        print()
        
        
    def Delete_Contact(self):
        print()
        self.con = sqlite3.connect(self.__URL)
        self.cur = self.con.cursor()
        
        id = int(input('Введіть ID контакта, який ви бажаєте видалити: '))
        self.cur.execute('''SELECT id, Name, PhoneNumber FROM Entries WHERE id == ?''',(id,))
        res = self.cur.fetchall()
        
        if res==[]: print('\n---Даного контакту немає АБО данні введені неправильно---\n')
        
        else:
            print('Видаляєм...')
            self.cur.execute('''DELETE FROM Entries WHERE id == ? ''',(id,))
            print('Контакт успішно видалено!')
        
        self.con.commit()
        self.con.close()
        print()
        
        
    def View_Contacts(self):
        print()
        self.con = sqlite3.connect(self.__URL)
        self.cur = self.con.cursor()
        
        self.cur.execute('SELECT id, Name, PhoneNumber FROM Entries')
        res = self.cur.fetchall()
        
        if res==[]: print('Контакти пусті\n')
        else:
            for id,name,phnm in res:
                print(f'ID:{id} | Name: {name:10} | Phone number: {phnm}')

        self.con.commit()
        self.con.close()
        print()




if __name__=="__main__":
    a = Telephon_program()