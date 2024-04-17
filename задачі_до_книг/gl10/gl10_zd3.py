# Information

class Information:
    
    def __init__(self, name, adres, age, tel_num) -> None:
        self.__name=name
        self.__adres=adres
        self.__age=age
        self.__tel_num=tel_num
        
    def set_name(self,name):
        self.__name=name
        
    def get_name(self):
        return self.__name
        
    def set_adres(self,adres):
        self.__adres=adres
    
    def get_adres(self):
        return self.__adres
    
    def set_age(self, age):
        self.__age=age
        
    def get_age(self):
        return self.__age
    
    def set_tel_num(self,tel_num):
        self.__tel_num=tel_num
        
    def get_tel_num(self):
        return self.__tel_num
    
    def __str__(self) -> str:
        return f'Імя {self.__name}\nАдреса {self.__adres}\nВік {self.__age}\nНомер телефону {self.__tel_num}'
    
    
def set_information():
    name=str(input('Введіть ваше імя: '))
    adres=str(input('Введіть вашу адресу: '))
    age=int(input('Введіть ваш вік: '))
    tel_num=str(input('Введіть ваш номер телефона: '))
    return name, adres, age, tel_num


def main():
    name, adres, age, tel_num=set_information()
    user1=Information(name, adres, age, tel_num)
    print(user1)
    
    name, adres, age, tel_num=set_information()
    user2=Information(name, adres, age, tel_num)
    print(user2)
    
    name, adres, age, tel_num=set_information()
    user3=Information(name, adres, age, tel_num)
    print(user3)
    
    
if __name__=='__main__':
    main()