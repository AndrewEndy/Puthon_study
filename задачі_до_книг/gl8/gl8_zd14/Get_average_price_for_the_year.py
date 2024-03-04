# Середня ціна за рік

from Get_value import get_value, count_of_years


def get_average_price_for_the_year():
    day_list,month_list,year_list,price_list=get_value()
    #print(price_list)
    flag_year=int(year_list[0])
    i=0
    sum_list=[]
    
    count=count_of_years()
    for el in range(0,count):
        count=0
        sum=0
        while flag_year==int(year_list[i]):
            #print(f'{year_list[i]} ---> {price_list[i]}')
            sum+=float(price_list[i])
            count+=1
            if price_list[i]==price_list[-1]: break
            else: i+=1
        #print(sum)
        flag_year+=1 
        sum=sum/count
        sum=f'{sum:.3f}'
        sum_list.append(sum)
        
    #print(sum_list) 
    return tuple(sum_list)


def print_get_average_price_for_the_year():
    price_sum_list=get_average_price_for_the_year()
    year=1993
    for i in range(0,21):
        print(f'{year} ---> {price_sum_list[i]}')
        year+=1    
        
        
def main():
    price_sum_list=get_average_price_for_the_year()
    year=1993
    for i in range(0,21):
        print(f'{year} ---> {price_sum_list[i]}')
        year+=1   
            

if __name__ == "__main__":
    main()
    