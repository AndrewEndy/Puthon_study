# Сума цифр в строці

def sum_nums_in_string(numb):
    res=0
    for num in numb:
        res+=int(num)
    return(res)

def main():
    numb=str(input('Веддіть ваше число: '))
    numb=numb.strip()
    res=sum_nums_in_string(numb)
    print(f'Сума кожної цифри в вашому числі: {res}')


if __name__ == "__main__":
    main()