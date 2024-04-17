# Car

class Car:
    
    def __init__(self, year_model, maker) -> None:
        self.__year_model=year_model
        self.__maker=maker
        self.__speed=0
        
    def get_speed(self):
        return self.__speed
    
    def accelerate(self):
        self.__speed+=5
        print(f'Швидкість становить: {self.get_speed()} кг/г\n')
        
    def break_speed(self):
        self.__speed-=5
        print(f'Швидкість становить: {self.get_speed()} кг/г\n')
        
    def __str__(self) -> str:
        return f'Рік випуску {self.__year_model}\nВиробник {self.__maker}\nШвидкість {self.__speed}'



def main():
    bmw = Car(1997, 'Germany')
    print(bmw)
    
    bmw.accelerate()
    bmw.accelerate()
    bmw.accelerate()
    bmw.accelerate()
    bmw.accelerate()
    
    bmw.break_speed()
    bmw.break_speed()
    bmw.break_speed()
    bmw.break_speed()
     
    print(bmw)
    


if __name__=='__main__':
    main()