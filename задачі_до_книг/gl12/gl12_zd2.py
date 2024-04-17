# Рекурсивное умножение

def func(x,y):
    if x!=0:
        return y + func(x-1,y)
    else: return 0


def main():
    x=int(input('Введіть число: '))
    y=int(input('Введіть число: '))
    print(func(x,y))


if __name__=='__main__':
    main()