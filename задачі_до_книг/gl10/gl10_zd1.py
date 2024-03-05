# class Pet


class Pet:
    
    def __init__(self, name=None, animal_type=None, age=None) -> None:
        self.__name=name
        self.__animal_type=animal_type
        self.__age=age
    
    def set_name(self,name):
        self.__name=name
    
    def get_name(self):
        return self.__name

    def set_animal_type(self, animal_type):
        self.__animal_type=animal_type
        
    def get_animal_type(self):
        return self.__animal_type

    def set_age(self, age):
        self.__age=age
        
    def get_age(self):
        return self.__age
    
    def __str__(self) -> str:
        return f'Назва тварини: {self.__name}\nТип тварини: {self.__animal_type}\nВік тварини: {self.__age}'


def main():
    name=str(input('Введіть імя: '))
    type_animal=str(input('Вкажіти тип тварини: '))
    age=int(input('Вкажіть вік тварини: '))

    pet=Pet(name, type_animal, age)
    print(pet)
    
    name=str(input('Введіть імя: '))
    pet.set_name(name)
    print(pet.get_name())
    
    type_animal=str(input('Вкажіти тип тварини: '))
    pet.set_animal_type(type_animal)
    print(pet.get_animal_type())
    
    age=int(input('Вкажіть вік тварини: '))
    pet.set_age(age)
    print(pet.get_age())

if __name__=='__main__':
    main()