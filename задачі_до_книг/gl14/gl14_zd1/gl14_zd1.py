# База данных населения
import sqlite3

class Program:
    def __init__(self) -> None:
        self.__URL='gl14/gl14_zd1/cities.db'
        self.menu()
        

    def menu(self):
        while True:
            print('----MENU----')
            print('1.Вывод на экран списка городов, отсортированных по численности населения в порядке возрастания')
            print('2.Вывод на экран списка городов, отсортированных по численности населения в порядке убывания')
            print('3.Bывод на экран списка городов, отсортированных по названиям')
            print('4.Bывод на экран общей численности населения всех городов')
            print('5.Bывод на экран среднего населения всех городов')
            print('6.Bывод на экран города с наибольшей численностью населения')
            print('7.Bывод на экран города с наименьшей численностью населения')
            print('8.Вихід')
            choice = int(input('Ваш вибір: '))
                
            if choice==1: self.Sort_by_Population_Ascending()
            if choice==2: self.Sort_by_Population_Descending()
            if choice==3: self.Sorted_List_of_Cities_by_Name()
            if choice==4: self.total_population_of_all_cities()
            if choice==5: self.Average_Population_of_All_Cities()
            if choice==6: self.cities_with_highest_population()
            if choice==7: self.cities_with_lowest_population()
            if choice==8: break



    def Sort_by_Population_Ascending(self):
        population_list,city_list,city_and_popul_dict = self.Data()
        population_list.sort()
        
        print(f'\n---ПО ЗРОСТАНЮ---')
        for i in population_list:
            print(f'{city_and_popul_dict.get(i):15} -----    {i}')
        print()
        
        
    def Sort_by_Population_Descending(self):
        population_list,city_list,city_and_popul_dict = self.Data()
        population_list.sort()
        population_list.reverse()
        
        print(f'\n---ПО СПАДАННЮ---')
        for i in population_list:
            print(f'{city_and_popul_dict.get(i):15} -----    {i}')
        print()
        
        
    def Sorted_List_of_Cities_by_Name(self):
        population_list,city_list,city_and_popul_dict = self.Data()
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        
        print('---ПО НАЗВАМ---')
        for word in alphabet:
            for city in city_list:
                if word == city[0]:
                    print(f'{city:15} -----   {get_key(city_and_popul_dict,city)}')
        print()
        
        
    def total_population_of_all_cities(self):
        population_list,city_list,city_and_popul_dict = self.Data()
        
        print()
        sum=0.0
        for el in population_list:
            sum+=el
        print(f'Спільна кількість населення всіх міст: {sum}\n')
        
        
    def Average_Population_of_All_Cities(self):
        population_list,city_list,city_and_popul_dict = self.Data()
        
        print()
        sum=0.0
        for el in population_list:
            sum+=el
        print(f'Середня кількість населення всіх міст: {sum/len(population_list)}\n') 
    
        
    def cities_with_highest_population(self):
        population_list,city_list,city_and_popul_dict = self.Data()
        population_list.sort()
        population_list.reverse()
        
        print(f'\nМісто з найбільшою кількістю населеня: {city_and_popul_dict.get(population_list[0])} ----- {population_list[0]}\n')
    
    
    def cities_with_lowest_population(self):
        population_list,city_list,city_and_popul_dict = self.Data()
        population_list.sort()
        
        print(f'\nМісто з найменшою кількістю населеня: {city_and_popul_dict.get(population_list[0])} ----- {population_list[0]}\n')
    
        
    def Data(self):
        self.con = sqlite3.connect(self.__URL)
        self.cur = self.con.cursor()
        
        self.cur.execute('SELECT CityName, Population FROM Cities')
        res = self.cur.fetchall()
        
        self.con.commit()
        self.con.close()
        
        city_and_popul_dict={}
        city_list=[]
        population_list=[]
        for city, popul in res:
            population_list.append(popul)
            city_list.append(city)
            city_and_popul_dict[popul] = city
        return population_list,city_list,city_and_popul_dict
        

def get_key(dictionary, value):
    for k, v in dictionary.items():
        if v == value:
            return k
    return None


if __name__=='__main__':
    a = Program()