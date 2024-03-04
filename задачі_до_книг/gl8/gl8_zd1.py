# Ініціали

def initials(FIO):
    fio_parts=FIO.split()
    res=''
    for part in fio_parts:
        part=part.upper()
        res+=part[0]+'.'
    return res


def main():
    FIO=str(input('Введіть ваше повне ФІО: '))
    res=initials(FIO) 
    print(f'Ваші ініціали: {res}')


if __name__ == "__main__":
    main()