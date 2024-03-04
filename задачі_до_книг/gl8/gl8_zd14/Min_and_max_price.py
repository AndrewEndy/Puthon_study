# Найбільша і найменша ціна в році

from Get_value import get_value, count_of_years


def get_min_price_of_year():
    day_list,month_list,year_list,price_list=get_value()
    #print(price_list)
    
    flag_year=int(year_list[0])
    i=0
    min_list=[]
    
    count=count_of_years()
    for el in range(0,count):
        min=100
        while flag_year==int(year_list[i]):
            #print(f'{year_list[i]} ---> {price_list[i]}')
            if min>float(price_list[i]): min=float(price_list[i])
            
            if price_list[i]==price_list[-1]:break
            else: i+=1
        flag_year+=1
        min_list.append(min) 
        
    #print(min_list)
    return tuple(min_list)


def get_max_price_of_year():
    day_list,month_list,year_list,price_list=get_value()

    flag_year=int(year_list[0])
    i=0
    max_list=[]

    count=count_of_years()
    for el in range(0,count):
        max=0
        while flag_year==int(year_list[i]):
            #print(f'{year_list[i]} ---> {price_list[i]}')
            if max<float(price_list[i]): max=float(price_list[i])
            
            if price_list[i]==price_list[-1]:break
            else: i+=1
        flag_year+=1
        max_list.append(max) 
        
    #print(max_list)
    return tuple(max_list)
    

def print_min_and_max_price_of_year():
    max_tuple=get_max_price_of_year()
    min_tuple=get_min_price_of_year()
    year=1993
    for i in range(0,21):
        print(f'{year} min --> {min_tuple[i]} | max --> {max_tuple[i]}')
        year+=1


def main():
    max_tuple=get_max_price_of_year()
    min_tuple=get_min_price_of_year()
    year=1993
    for i in range(0,21):
        print(f'{year} min --> {min_tuple[i]} | max --> {max_tuple[i]}')
        year+=1


if __name__ == "__main__":
    main()