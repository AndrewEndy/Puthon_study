# Найчастіший символ

def get_most_frequent_str(s):
    s_max=0
    el_max=''
    for el in s:
        if s_max<s.count(el):
            s_max=s.count(el)
            el_max=el
    return s_max, el_max
            

def main():
    s=str(input('Введіть ваше повідомлення: '))
    res_n,res_s=get_most_frequent_str(s)
    print(f'Найчастіше в цьому повідомлені з\'являвся симлов ---> \'{res_s}\'   {res_n} <--- Стільки раз')    


if __name__ == "__main__":
    main()