# Retailltem

class Retailltem:
    def __init__(self, num_article=None, description=None, units_in_stock=None, price=None) -> None:
        self.__num_article=num_article
        self.__description=description
        self.__units_in_stock=units_in_stock
        self.__price=price
        
    def set_description(self,description):
        self.__description=description
    
    def get_description(self):
        return self.__description

    def set_units_in_stock(self,units_in_stock):
        self.__units_in_stock=units_in_stock
        
    def get_units_in_stock(self):
        return self.__units_in_stock
    
    def set_price(self, price):
        self.__price=price
        
    def get_price(self):
        return self.__price
    
    def get_num_article(self):
        return self.__num_article
        
    def __str__(self) -> str:
        return f'Номер товара: {self.__num_article}\nОпис:{self.__description}\nКількість на складі: {self.__units_in_stock}\nЦіна: {self.__price}'
  
    
def get_info():
    description=str(input('Введіть опис товару: '))
    units_in_stock=int(input('Введіть кількість товару: '))
    price=float(input('Введіть ціну: '))
    return description, units_in_stock, price
    
def for_zd8():
    retailltem_list=[]
    user1=Retailltem(1,'Піджак', 12, 59.95)
    retailltem_list.append(user1)
    
    user2=Retailltem(2,'Дизайнерські джинси', 40, 34.95)
    retailltem_list.append(user2)
    
    user3=Retailltem(3,'Рубашка', 20, 24.95)
    retailltem_list.append(user3)
    return retailltem_list

def create_new_retailltem(num_article,description, units_in_stock, price):
    retailltem=Retailltem(num_article,description, units_in_stock, price)
    return retailltem
    

def main():
    retailltem_list=[]
    description, units_in_stock, price=get_info()
    user1=Retailltem(1,description, units_in_stock, price)
    retailltem_list.append(user1)
    
    description, units_in_stock, price=get_info()
    user2=Retailltem(2,description, units_in_stock, price)
    retailltem_list.append(user2)
    
    description, units_in_stock, price=get_info()
    user3=Retailltem(3,description, units_in_stock, price)
    retailltem_list.append(user3)
    
    for retailltem in retailltem_list:
        print(f'\n{retailltem}')


if __name__=='__main__':
    main()