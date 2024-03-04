# Отримати витягнуті значення

def get_value():
    file=open('gl8/gl8_zd14/GasPrices.txt','r')
    price=[]
    day=[]
    month=[]
    year=[]
    for line in file:
        # Витягуємо всі значення
        line=line.rstrip('\n')
        mas=line.split(':')
        date=mas[0]
        date_list=date.split('-')
        day.append(date_list[1])
        month.append(date_list[0])
        year.append(date_list[2])
        price.append(mas[1])
    return day, month, year, price


def count_of_years():
    day_list,month_list,year_list,price_list=get_value()
    count=0
    for year in year_list:
        if count==0:
            check=year
            count=1
        if check!=year: 
            count+=1
            check=year
    return count


def count_of_month():
    day_list,month_list,year_list,price_list=get_value()
    count=0
    for month in month_list:
        if count==0:
            check=month
            count=1
        if check!=month: 
            count+=1
            check=month
    return count


def main():
    #print(get_value())
    day_list,month_list,year_list,price_list=get_value()
    print(month_list)
    

if __name__=='__main__': main()