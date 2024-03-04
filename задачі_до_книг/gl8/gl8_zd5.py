# Алфавіт переводчик номера телефона

def number_translator(num):
    
    if len(num)>12:
        return 'Ви ввели невірний номер'
    
    ABC_dict={ 'A':'2', 'B':'2', 'C':'2', 'D':'3', 'E':'3', 'F':'3', 'G':'4', 'H':'4', 'I':'4', 'L':'5', 'K':'5', 'J':'5' ,'M':'6'
              , 'N':'6', 'O':'6', 'P':'7', 'Q':'7', 'R':'7', 'S':'7', 'T':'8', 'U':'8', 'V':'8', 'W':'9', 'X':'9', 'Y':'9', 'Z':'9' }
    
    num=num.upper()
    res=''
    flag=False
    for el in num:
        for key in ABC_dict.keys():
            if el==key:
                flag=True
                res+=ABC_dict.get(key)
        if flag==False:
            res+=el
        flag=False
    return res
                
    

def main():
    q=0
    while q!=1:
        num=str(input('Ввндіть номер телефона ( типу XXX-XXX-XXXX ): '))
        res=number_translator(num)
        if res=='Ви ввели невірний номер':
            print(res)
        else:
            print(f'Розшифрований номер: {res[0:3]}-{res[4:7]}-{res[8:]}')
        q=int(input('Закінчити(1): '))


if __name__ == "__main__":
    main()