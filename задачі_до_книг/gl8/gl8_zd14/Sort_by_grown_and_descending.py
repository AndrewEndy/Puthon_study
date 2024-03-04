# Список цін посортований по возростанию и убиванию
from Get_value import get_value


def create_sort_by_growth():
    day_list,month_list,year_list,price_list=get_value()

    index=len(day_list)
    min_price=[]
    date_list=[]

    while len(min_price)!=index:
        min=100
        for i in range(len(day_list)):
            if min>float(price_list[i]):
                min=float(price_list[i])
                min_index=price_list.index(str(min))
        min_price.append(price_list.pop(min_index))
        date_list.append(f'{year_list.pop(min_index)}-{month_list.pop(min_index)}-{day_list.pop(min_index)}')

    sort_by_growth_dict={}
    for i in range(len(min_price)):
        sort_by_growth_dict[f'{date_list[i]}']=min_price[i]
        
    file=open('gl8/gl8_zd14/Sort_by_growth.txt','w')
    for key,value in sort_by_growth_dict.items():
        file.writelines(f'{key}:{value}\n')
    file.close()


def create_sort_by_decline():
    day_list,month_list,year_list,price_list=get_value()

    index=len(day_list)
    max_price=[]
    date_list=[]

    while len(max_price)!=index:
        max=0
        for i in range(len(day_list)):
            if max<float(price_list[i]):
                max=float(price_list[i])
                max_index=price_list.index(str(max))
        max_price.append(price_list.pop(max_index))
        date_list.append(f'{year_list.pop(max_index)}-{month_list.pop(max_index)}-{day_list.pop(max_index)}')

    sort_by_decline_dict={}
    for i in range(len(max_price)):
        sort_by_decline_dict[f'{date_list[i]}']=max_price[i]
        
    file=open('gl8/gl8_zd14/Sort_by_decline.txt','w')
    for key,value in sort_by_decline_dict.items():
        file.writelines(f'{key}:{value}\n')
    file.close()



def main():
    create_sort_by_growth()
    create_sort_by_decline()
    

if __name__ == "__main__":
    main()