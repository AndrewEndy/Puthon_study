# Классы Person и Customer

class Person:
    def __init__(self, name, adres, tel_num) -> None:
        self.__name=name
        self.__adres=adres
        self.__tel_num=tel_num
        
    def set_name(self, name):
        self.__name=name
    
    def get_name(self):
        return self.__name
    
    def set_adres(self,adres):
        self.__adres=adres
    
    def get_adres(self):
        return self.__adres
    
    def set_tel_num(self,tel_num):
        self.__tel_num=tel_num
        
    def get_tel_num(self):
        return self.__tel_num
    
    def __str__(self) -> str:
        return f'Імя: {self.__name}\nАдреса: {self.__adres}\nНомер телефона: {self.__tel_num}\n'
        
class Customer(Person):
    def __init__(self, name, adres, tel_num,num_of_client, bool_rozcilka) -> None:
        super().__init__(name, adres, tel_num)
        self.__num_of_client=num_of_client
        self.__bool_rozcilka=bool_rozcilka
        
    def set_num_of_client(self,num_of_client):
        self.__num_of_client=num_of_client
    
    def get_num_of_client(self):
        return self.__num_of_client
    
    def set_bool_rozcilka(self,bool_rozcilka):
        self.__bool_rozcilka=bool_rozcilka
        
    def get_bool_rozcilka(self):
        return self.__bool_rozcilka
    
    def __str__(self) -> str:
        return super().__str__() + \
            f'Номер клієнта: {self.__num_of_client}' + \
            f'Розсилка: {self.__bool_rozcilka}'
        

def main():
    name=str(input('name: '))
    adres=str(input('adres: '))
    tel_num=str(input('tel num:'))
    num_of_client=int(input('num of client: '))
    bool_rozcilkf=bool(input('Розсилки: '))
    
    us1=Customer(name,adres,tel_num,num_of_client,bool_rozcilkf)
    print(us1)


if __name__=='__main__':
    main()