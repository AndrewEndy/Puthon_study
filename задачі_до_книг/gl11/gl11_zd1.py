# Классы Employee и ProductionWorker

class Employee:
    def __init__(self,name,number) -> None:
        self.__name=name
        self.__number=number
    
    def set_name(self,name):
        self.__name=name
    
    def get_name(self):
        return self.__name
    
    def set_number(self,number):
        self.__number=number
    
    def get_number(self):
        return self.__number

    def __str__(self) -> str:
        return f'Імя працівника: {self.__name}\nНомер працівника: {self.__number}\n'


class ProductionWorker(Employee):
    def __init__(self, name, number,work_number, hourly_wage_rate) -> None:
        Employee.__init__(self,name, number)
        self.__work_number=work_number
        self.__hourly_wage_rate=hourly_wage_rate
        
    def set_work_number(self,work_number):
        self.__work_number=work_number
    
    def get_work_number(self):
        return self.__work_number
    
    def set_hourly_wage_rate(self,hourly_wage_rate):
        self.__hourly_wage_rate=hourly_wage_rate
        
    def get_hourly_wage_rate(self):
        return self.__hourly_wage_rate
    
    def __str__(self) -> str:
        return super().__str__() + f'Номер змінни: {self.__work_number}\nСтавка почасової оплати: {self.__hourly_wage_rate}'
        

def create_ProductionWorker(n):
    worker_list=[]
    for worker in range(n):
        name=str(input('Введіть імя: '))
        number=int(input('Введіть номер працавника: '))
        work_number=int(input('Введіть номер змінни (1-Денна, 2-Нічна): '))
        if work_number>2 or work_number<1:
            print('Ви ввели невірну змінну')
            continue
        hourly_wage_rate=float(input('Введіть почасову оплату праці: '))
        worker=ProductionWorker(name, number, work_number, hourly_wage_rate)
        worker_list.append(worker)
    return worker_list


def main():
    n=int(input('Скільки раз заповняти данні: '))
    worker_list=create_ProductionWorker(n)
    
    for worker in worker_list:
        print(worker)


if __name__=='__main__':
    main()