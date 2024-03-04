# Голосні і приголосні

def vowels(s):
    vowels_num=0
    vowels_tuple=('а','е','и','і','о','у')
    for el in s:
        for i in vowels_tuple:
            if el.lower()==i:
                vowels_num+=1
    return vowels_num


def consonants(s):
    consonants_num=0
    consonants_tuple=('б', 'в', 'г', 'ґ', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')
    for el in s:
        for i in consonants_tuple:
            if el.lower()==i:
                consonants_num+=1
    return consonants_num


def soft_consonant(s):
    soft_consonant_num=0
    soft_consonant_tuple=('я','ю','ї','є')
    for el in s:
        for i in soft_consonant_tuple:
            if el.lower()==i:
                soft_consonant_num+=1
    return soft_consonant_num


def main():
    s=str(input('Введіть ваше повідомлення: '))
    vowels_num=vowels(s)
    consonants_num=consonants(s)
    soft_consonant_num=soft_consonant(s)
    print(f'Кількість голосних букв: {vowels_num}\nКількість приголосних букв: {consonants_num}\nКількість м\'яких приголосних: {soft_consonant_num}')


if __name__ == "__main__":
    main()