# Переможці світової серії


def get_year_win():
    file = open('gl9/WorldSeriesWinners.txt','r')
    year=1903
    res_dict={}
    
    for line in file:
        line=line.strip()
        if line=='World Series Not Played in 1904' or line=='World Series Not Played in 1994': res_dict[year]='Ігри не проводились'
        else:res_dict[year]=line
        year+=1
    return res_dict
    #for key,val in res_dict.items():
        #print(f'{key} ---> {val}')
            
            
def get_dict_count_of_wins():
    file = open('gl9/WorldSeriesWinners.txt','r')
    s=file.read()
    s=s.split('\n')
    s.remove('World Series Not Played in 1904')
    s.remove('World Series Not Played in 1994')
    s_set=set(s)
    
    count_of_wins_dict={}
    for el in s_set:
        count_of_wins_dict[el]=s.count(el)
    return count_of_wins_dict
    #for key, val in count_of_wins_dict.items():
        #print(f'{key} ---> {val}')
        
        
def print_my_input_year():
    year=int(input('Введіть рік від 1993 до 2009: '))
    year_dict=get_year_win()
    count_dict=get_dict_count_of_wins()
    
    if year==1904 or year==1994:return 'Гра не відбулась'
    
    index=year_dict[year]
    return f'{index} ---> {count_dict[index]}'
    


def main():
    year_dict=get_year_win()
    for key,val in year_dict.items():
        print(f'{key} ---> {val}')
    print()
    count_dict=get_dict_count_of_wins()
    for key, val in count_dict.items():
        print(f'{key} ---> {val}')
    print()
    print(print_my_input_year())

if __name__=='__main__':
    main()