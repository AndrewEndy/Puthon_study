# Упражнение по программированию 8.3

# Принтер дат

def main():
    # Локальные переменные
    day = 0
    month_num = 0
    month_name = ''
    date_string = ''
    month_list = ['января', 'февраля','марта',
                  'апреля', 'мая','июня', 'июля',
                  'августа', 'сентября', 'октября',
                  'ноября', 'декабря']
    
    # Получить от пользователя дату в формате дд/мм/гггг.
    date_string = input('Введите дату в формате дд/мм/гггг: ')

    # Разбить строку с датой date_string.
    date_list = date_string.split('/')

    # Получить номера месяца и дня.
    day = date_list[0]
    month_num = int(date_list[1])
    year = date_list[2]

    # Получить название месяца.
    month_name = month_list[month_num - 1]

    # Создать строковое значение для даты в длинном формате.
    long_date = day + ' ' + month_name + ' ' + year + ' г.'

    # Показать дату в длинном формате.
    print(long_date)

# Вызвать главную функцию.
main()