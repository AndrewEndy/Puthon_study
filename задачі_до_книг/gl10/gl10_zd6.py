# Расходы на лечение

class Patient:
    def __init__(self, FIO, AGP, tel_num, extra_name_tel) -> None:
        self.__FIO=FIO
        self.__AGP=AGP
        self.__tel_num=tel_num
        self.__extra_name_tel=extra_name_tel
        
    def __str__(self) -> str:
        return f'ФИО: {self.__FIO}\nАдрес, город, область и почтовый индекс: {self.__AGP}\nНомер телефону: {self.__tel_num}\nИмя и телефон контактного лица для экстренной связи: {self.__extra_name_tel}\n'
    
    
class Procedure:
    def __init__(self, name_of_procedure, date_of_procedure, name_doctor, price) -> None:
        self.__name_of_procedure=name_of_procedure
        self.__date_of_procedure=date_of_procedure
        self.__name_doctor=name_doctor
        self.__price=price
    
    def get_price(self):
        return self.__price
    
    
    def __str__(self) -> str:
        return f'Назва процедури: {self.__name_of_procedure}\n' + \
        f'Дата процедури: {self.__date_of_procedure}\n' + \
        f'Імя врача: {self.__name_doctor}\n' + \
        f'Ціна процедури: {self.__price}\n'
        

def get_procedure_info():
    name_of_procedure=str(input('Введіть назву процедури: '))
    date_of_procedure=str(input('Введіть дату процедури: '))
    name_doctor=str(input('Введіть імя врача: '))
    price=float(input('Введіть ціну процедури: '))
    return name_of_procedure, date_of_procedure, name_doctor, price


def get_patient_info():
    FIO=str(input('Введіть ваше ФІО: '))
    AGP=str(input('Введіть адрес, город, область и почтовый индекс: '))
    tel_num=str(input('Введіть ваш номер телефону: '))
    extra_name_tel=str(input('Имя и телефон контактного лица для экстренной связи: '))
    return FIO, AGP, tel_num, extra_name_tel

def main():
    FIO, AGP, tel_num, extra_name_tel=get_patient_info()
    patient1=Patient(FIO, AGP, tel_num, extra_name_tel)
    
    procedure_list=[]
    name_of_procedure, date_of_procedure, name_doctor, price=get_procedure_info()
    procedure1=Procedure(name_of_procedure, date_of_procedure, name_doctor, price)
    procedure_list.append(procedure1)
    
    name_of_procedure, date_of_procedure, name_doctor, price=get_procedure_info()
    procedure2=Procedure(name_of_procedure, date_of_procedure, name_doctor, price)
    procedure_list.append(procedure2)
    
    name_of_procedure, date_of_procedure, name_doctor, price=get_procedure_info()
    procedure3=Procedure(name_of_procedure, date_of_procedure, name_doctor, price)
    procedure_list.append(procedure3)
    
    print(patient1)
    
    count=0
    for procedure in procedure_list:
        print()
        print(procedure)
        count+=procedure.get_price()

    print(f'\nСумарна ціна: {count}')

if __name__=='__main__':
    main()