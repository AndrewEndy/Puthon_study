# Рекурсивная печать


def func(n,i=1):
    if n!=0:
        print(i)
        func(n-1,i+1)

def main():
    n=int(input('Введіть число: '))
    func(n)


if __name__=='__main__':
    main()