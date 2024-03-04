# Імена та адреси електроних почт

def main_function():
    file=open('gl9/gl9_zd8.txt','r',encoding='utf-8')
    name_email_dict={}
    for line in file:
        s=line.split()
        name_email_dict[s[0]]=(s[1])
    file.close() 
    #print(name_email_dict)

    index=''
    while index!='end':
        print(f'---MENU---\n1.Відшукати електроний адрес по імені\n2.Додати нові дані\n3.Змінити електрону адресу або ім\'я\n4.Видалити дані\n5.Вивести базу даних\n6.Вихід')
        try:
            choice=int(input('Вибір: '))
            if choice<1 or choice>6:
                print('---> Ви ввели невірне число\n')
                continue
        except ValueError:
            print('---> Ви ввели не той тип данниx число\n')
            continue
        
        if choice==1:
            name=str(input('Введіть ім\'я: '))
            if name in name_email_dict:print(f'Ім\'я: {name} --- Електрона адреса: {name_email_dict[name]}\n')
            else: print('Даного імені нема в базі')
            print()
            continue
        
        if choice==2:
            name=str(input('Введіть ім\'я: '))
            if name in name_email_dict:
                print('Це ім\'я вже є в базі даних\n')
                continue
            else:
                email=str(input('Введіть електрону адрусу: '))
                name_email_dict[name]=email
                print()
                continue
        
        if choice==3:
            name=str(input('Введіть ім\'я: '))
            print('1.Змінити ім\'я\n2.Змінити email')
            choi=int(input('Ваш вибір: '))
            if choi>2 or choi<1:
                print('Ви ввели не те число\n')
                continue
            
            if choi==1:
                email=name_email_dict[name]
                name_email_dict.pop(name)
                name=str(input('Введіть нове ім\'я: '))
                name_email_dict[name]=email
                print()
                continue
            if choi==2:
                email=str(input('Введіть новий електроний адрес: '))
                name_email_dict[name]=email
                print()
                continue
        
        if choice==4:
            name=str(input('Введіть ім\'я: '))
            if name in name_email_dict:name_email_dict.pop(name)
            else:print('Даного імені нема в базі')            
            print()
            continue
        
        if choice==5:
            print()
            for key,val in name_email_dict.items():
                print(f'{key} --- {val}')
            print()
            continue
        
        if choice==6:
            print('Вихід...')
            file=open('gl9/gl9_zd8.txt','w',encoding='utf-8')
            for key,val in name_email_dict.items():
                file.write(f'{key} {val}\n')
            index='end'
            file.close()
   


def main():
    main_function()


if __name__=='__main__':
    main()