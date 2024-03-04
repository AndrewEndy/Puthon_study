# Cередня ціна за місяць в кожному році

from Get_value import get_value, count_of_month


def get_average_price_per_month():
    day_list,month_list,year_list,price_list=get_value()

    flag_month=int(month_list[0])
    i=0
    sum_dict={}

    count=count_of_month()
    for el in range(0,count):
        sum=0
        count=0
        while flag_month==int(month_list[i]):
            sum+=float(price_list[i])
            count+=1
            if price_list[i]==price_list[-1]: break
            else: i+=1
        sum=sum/count
        sum=f'{sum:.3f}'
        sum_dict[f'{year_list[i-1]}-{month_list[i-1]}']=sum
        if flag_month==12: flag_month=1
        else: flag_month+=1
    #print(sum_dict)
    return sum_dict


def print_get_average_price_per_month():
    sum_dict=get_average_price_per_month()
    for key,value in sum_dict.items():
        print(f'{key} ---> {value}')
    
    
def main():
    sum_dict=get_average_price_per_month()
    for key,value in sum_dict.items():
        print(f'{key} ---> {value}')
        
        
if __name__=='__main__': main()