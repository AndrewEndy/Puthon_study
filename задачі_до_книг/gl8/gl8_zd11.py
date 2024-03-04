# Розділитель слів


def separator(s):
    res=s[0]
    s=s[1:]
    
    for el in s:
        if el.isupper():
            res+=' '+el.lower()
        else:
            res+=el
    return res
    


def main():
    s=str(input('Введіть ваше повідомлення: '))
    res=separator(s)
    print(f'Розділене повідомлення: {res}')
    


if __name__ == "__main__":
    main()