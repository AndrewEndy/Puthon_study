# Аналіз файла

def analysis_file():
    file=open('gl8/gl8_zd6.txt','r',encoding='utf-8')
    s=file.read()
    file.close()
    
    el_upper=0
    el_lower=0
    el_num=0
    el_space=0
    
    for el in s:
        if el.isupper():
            el_upper+=1
        elif el.islower():
            el_lower+=1
        elif el.isdigit():
            el_num+=1
        elif el==' ':
            el_space+=1
    return [el_upper,el_lower,el_num,el_space]


def main():
    res=analysis_file()
    print(f'Букви в верхньому регістрі: {res[0]}\nБукви у нижньому регістрі: {res[1]}\nКількість чисел: {res[2]}\nКількість пробілів: {res[3]}')


if __name__ == "__main__":
    main()