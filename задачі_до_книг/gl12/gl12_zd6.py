# Сумма чисел


def func(n):
    if n!=0:
        return n + func(n-1)
    else: return 0



def main():
    n=int(input('Введіть число: '))
    print(func(n))


if __name__=='__main__':
    main()