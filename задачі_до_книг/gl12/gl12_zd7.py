#  Рекурсивный метод возведения в степень


def func(x,y):
    if y!=0:
        return x * func(x,y-1)
    else: return 1

def main():
    x=int(input('Введіть число: '))
    y=int(input('Введіть число: '))
    print(func(x,y))


if __name__=='__main__':
    main()