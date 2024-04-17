#Функция Аккерманна


def ackermann(m,n):
    if m==0:
        return n+1
    if n==0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1,ackermann(m,n-1))


def main():
    m=int(input('Введіть число: '))
    n=int(input('Введіть число: '))
    print(ackermann(m,n))


if __name__=='__main__':
    main()