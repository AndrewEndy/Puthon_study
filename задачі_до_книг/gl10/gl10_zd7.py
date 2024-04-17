# Система управления персоналом

import gl10_zd4 as gle

def personnel_management_system():
    gle.for_zd7()
    file=open('gl10/gl10_for_zd7.txt','r',encoding='utf-8')
    employee_dict={}
    
    for line in file:
        line=line.split()
        name=line[0]+' '+line[1]
        id=int(line[2])
        viddil=line[3]
        dol=line[4]
        employee = gle.Employee(name, id, viddil, dol)
        employee_dict[employee.get_id()]=employee
    file.close()
    
    index='д'
    while index=='д':
        choice=Menu()
        
        if choice == 1:
            id=int(input('Введіть id сотрудника: '))
            if id in employee_dict:
                print(f'\n{employee_dict[id]}')
            else:
                print(f'\nДаного сотрудника немає')
            
        if choice==2:
            employee=gle.create_new_employee()
            if employee.get_id() in employee_dict.keys():print('\nДаний сотрудник уже є')
            else:employee_dict[employee.get_id()]=employee
            
        if choice==3:
            id=int(input('Введіть id сотрудника: '))
            if id in employee_dict:
                empolyee=gle.correct_employee(id)
                employee_dict[id]=empolyee
            else:
                print(f'\nДаного сотрудника немає')
                
        if choice==4:
            id=int(input('Введіть id сотрудника: '))
            if id in employee_dict:
                employee_dict.pop(id)
            else:
                print(f'\nДаного сотрудника немає')     
        
        if choice==5:
            file=open('gl10/gl10_for_zd7.txt','w',encoding='utf-8')
            for employee in employee_dict.values():
                file.write(f'{employee.get_name()} {employee.get_id()} {employee.get_viddil()} {employee.get_dol()}\n')
            file.close()
            index='н'
        
        
def Menu():
    print(f'\nMENU')
    print(f'-------------------')
    print(f'1.найти сотрудника в словаре')
    print(f'2.добавить нового сотрудника в словарь')
    print(f'3.изменить имя, отдел и должность существующего сотрудника в словаре')
    print(f'4.удалить сотрудника из словаря')
    print(f'5.выйти из программы')
    choice=int(input('Вибір: '))
    return choice
    

def main():
    personnel_management_system()
    


if __name__=='__main__':
    main()