# Вікторина по столицям
import random


def quiz():
    country_and_capital={'Болгарія':'Софія', 'Німечина':'Берлін', 'Франція':'Париж', 'Швеція':'Стокгольм', 'Італія':'Рим'
                         , 'Англія':'Лондон', 'Білорусь':'Мінск', 'Японія':'Токіо', 'Мексика':'Мехіко', 'Бразилія':'Бразиліа'}
    index_list=[]
    for val in country_and_capital.keys():
        index_list.append(val)
    right=0
    wrong=0
    random_country=random.sample(index_list,len(index_list))
    for i in random_country:
        index=str(input(f'Введіть столицю цієї країни {i}: '))
        
        if index.lower() == (country_and_capital[i]).lower():
            right+=1
        else:
            wrong+=1
    return right,wrong


def main():
    right,wrong=quiz()
    print(f'Кількість правильних відповідей: {right}\nКількість не правильних відповідей: {wrong} ')


if __name__=='__main__':
    main()