# Класс ShiftSupervisor
from gl11_zd1 import Employee

class ShiftSupervisor(Employee):
    def __init__(self, name, number,annual_salary,annual_bonus) -> None:
        Employee.__init__(self, name, number)
        self.__annual_salary=annual_salary*2080
        self.__annual_bonus=annual_bonus
        
    def set_annual_salary(self,annual_salary):
        self.__annual_salary=annual_salary*2080
        
    def get_annual_salary(self):
        return self.__annual_salary
    
    def set_annual_bonus(self,annual_bonus):
        self.__annual_bonus=annual_bonus
    
    def get_annual_bonus(self):
        return self.__annual_bonus
    
    def __str__(self) -> str:
        return Employee.__str__(self) + f'Годовой оклад: {self.__annual_salary}\nРічна премія: {self.__annual_bonus}'
   
    
def create_ShiftSupervisor(n):
    ShiftSupervisor_list=[]
    for Supervisor in range(n):
        name=str(input('Введіть імя: '))
        number=int(input('Введіть номер працавника: '))
        salary=float(input('Введіть вашу почасову ставку: '))
        annual_bonus=float(input('Введіть премію: '))
        Supervisor = ShiftSupervisor(name,number,salary, annual_bonus)
        ShiftSupervisor_list.append(Supervisor)
    return ShiftSupervisor_list


def main():
    n=int(input('Скільки раз вводити дані: '))
    ShiftSupervisor_list=create_ShiftSupervisor(n)
    
    for i in ShiftSupervisor_list:
        print('\n',i)
    
if __name__=='__main__':
    main()