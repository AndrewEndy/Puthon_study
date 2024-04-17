# Employee

class Employee:
    def __init__(self, name, id, viddil, dol) -> None:
        self.__name=name
        self.__id=id
        self.__viddil=viddil
        self.__dol=dol
        
    def set_name(self,name):
        self.__name=name
        
    def get_name(self):
        return self.__name
    
    def set_id(self, id):
        self.__id=id
        
    def get_id(self):
        return self.__id
    
    def set_viddil(self, viddil):
        self.__viddil=viddil
        
    def get_viddil(self):
        return self.__viddil
    
    def set_dol(self, dol):
        self.__dol=dol
        
    def get_dol(self):
        return self.__dol
    
            
    def __str__(self) -> str:
        return f'Імя: {self.__name}\nІдентифікаційний код: {self.__id}\nВідділ: {self.__viddil}\nПосада: {self.__dol}'
    

def get_info():
    name=str(input('Введіть імя: '))
    id=int(input('Введіть id: '))
    viddil=str(input('Вкажіть відділ: '))
    dol=str(input('Введіть посаду: '))
    return name, id, viddil, dol


def create_new_employee():
    name, id, viddil, dol=get_info()
    employee=Employee(name, id, viddil, dol)
    return employee

def correct_employee(id):
    name=str(input('Введіть нове імя: '))
    viddil=str(input('Вкажіть новий відділ: '))
    dol=str(input('Введіть нову посаду: '))
    employee=Employee(name, id, viddil,dol)
    return employee
    

    
def for_zd7():
    file=open('gl10/gl10_for_zd7.txt','w',encoding='utf-8')
    employee1=Employee('Сьюзан Мейерс',47899,'Бухгалтерия','Вице-президент')
    employee2=Employee('Mарк Джоунс',39119,'IT','Программист')
    employee3=Employee('Джой Роджерс',81774,'Производствений','Инженер')
    file.write(f'{employee1.get_name()} {employee1.get_id()} {employee1.get_viddil()} {employee1.get_dol()}\n')
    file.write(f'{employee2.get_name()} {employee2.get_id()} {employee2.get_viddil()} {employee2.get_dol()}\n')
    file.write(f'{employee3.get_name()} {employee3.get_id()} {employee3.get_viddil()} {employee3.get_dol()}\n')
    file.close()

def main():
    employee_list=[]
    name, id, viddil, dol = get_info()
    user1=Employee(name, id, viddil, dol)
    employee_list.append(user1)
    
    name, id, viddil, dol = get_info()
    user2=Employee(name, id, viddil, dol)
    employee_list.append(user2)
    
    name, id, viddil, dol = get_info()
    user3=Employee(name, id, viddil, dol)
    employee_list.append(user3)
    
    for employee in employee_list:
        print()
        print(employee)
    


if __name__=='__main__':
    main()