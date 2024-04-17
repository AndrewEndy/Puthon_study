# Класс CashRegister

import gl10_zd5 as gle


class CashRegister:
    def __init__(self,retailltem_list) -> None:
        self.__retailltem_list=retailltem_list
        self.__basket=[]
        self.__num=1
        
    def __str__(self) -> str:
        return f'{self.__retailltem_list}'
    
    def show_basket(self):
        print(f'\n-----Кошик-----')
        if self.__basket==[]:
            print(f'Пустий')
        else:
            for retailltem in self.__basket:
                print(f'{retailltem}\n')

    def purchase_item(self):
        print(f'\nЯкий товар хочете придбати:')
        count=1
        for retailltem in self.__retailltem_list:
            print(f'{count}.{retailltem.get_description()}')
            count+=1
        choice=int(input('Вибір: '))
        count=int(input('Яку кількість: '))
        if choice==1 and count<=self.__retailltem_list[0].get_units_in_stock():
            basket_retailltem=gle.create_new_retailltem(self.__num,self.__retailltem_list[0].get_description(),count,self.__retailltem_list[0].get_price())
            self.__basket.append(basket_retailltem)
            temp_count=self.__retailltem_list[0].get_units_in_stock()
            self.__retailltem_list[0].set_units_in_stock(temp_count-count)
            print()
        if choice==1 and count>self.__retailltem_list[0].get_units_in_stock():
            print('\nДаної кількості товару немає')
        
        if choice==2 and count<=self.__retailltem_list[1].get_units_in_stock():
            basket_retailltem=gle.create_new_retailltem(self.__num,self.__retailltem_list[1].get_description(),count,self.__retailltem_list[1].get_price())
            self.__basket.append(basket_retailltem)
            temp_count=self.__retailltem_list[1].get_units_in_stock()
            self.__retailltem_list[1].set_units_in_stock(temp_count-count)
            print()
        if choice==2 and count>self.__retailltem_list[1].get_units_in_stock():
            print('\nДаної кількості товару немає')
        
        if choice==3 and count<=self.__retailltem_list[2].get_units_in_stock():
            basket_retailltem=gle.create_new_retailltem(self.__num,self.__retailltem_list[2].get_description(),count,self.__retailltem_list[2].get_price())
            self.__basket.append(basket_retailltem)
            temp_count=self.__retailltem_list[2].get_units_in_stock()
            self.__retailltem_list[2].set_units_in_stock(temp_count-count)
            print()
        if choice==3 and count>self.__retailltem_list[2].get_units_in_stock():
            print('\nДаної кількості товару немає')
        self.__num+=1

    def show_items(self):
        print('\n----Список всіх товарів----')
        for retailltem in self.__retailltem_list:
            print(f'{retailltem}\n')
            
    def clear_basket(self):
        self.__basket=[]
        self.show_basket()
        
    def get_total(self):
        self.show_basket()
        res_sum=0
        for retailltem in self.__basket:
            res_sum+=(retailltem.get_price()*retailltem.get_units_in_stock())
        print(f'\nСума всієї покупки: {res_sum}')
                
        
    
    
def menu():
    print(f'\n-----MENU-----')    
    print(f'1.Придбати товар')
    print(f'2.Отримати суму купівлі')
    print(f'3.Показати наявні товари')
    print(f'4.Очистити кошик')
    print(f'5.Подивитись кошик')
    print(f'6.Вихід')
    choice=int(input('Вибір: '))
    return choice
    
        
    
def gl_function():
    retailltem_list=gle.for_zd8()
    cash_register=CashRegister(retailltem_list)
    
    index='д'
    while index=='д':
        choice=menu()
        
        if choice==1:cash_register.purchase_item()
        
        if choice==2:cash_register.get_total()        
        
        if choice==3:cash_register.show_items()
        
        if choice==4:cash_register.clear_basket()
        
        if choice==5:cash_register.show_basket()
        
        if choice==6: index='1'
    
    
    
def main():
    gl_function()
    
    
if __name__=='__main__':
    main()