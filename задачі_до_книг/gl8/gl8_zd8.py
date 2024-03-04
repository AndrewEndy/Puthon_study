# Коректор предложений

def corrector(s):
    s.lower()
    s_list=s.split()
    res=''
    flag=False
    
    first_word=s_list.pop(0)
    res+=first_word.capitalize()+' ' # Робим щоб перше слово весь час починалось з великої букви
    if first_word[-1]=='.' or first_word[-1]=='!' or first_word[-1]=='?' or first_word[-2:]=="?!" or first_word[-2:]=='!?': # Провірка на . ! ? і тд
            flag=True
    
    for el in s_list: # Цикл робить щоб кожне речення починалось з великої букви
        if flag==True:
            res+=el.capitalize()+' '
            flag=False
        else:
            res+=el+' '
            
        if el[-1]=='.' or el[-1]=='!' or el[-1]=='?' or el[-2:]=="?!" or el[-2:]=='!?':
            flag=True
    
    return res
            

def main():
    s=str(input('Введіть ваше повідомлення: '))
    res=corrector(s)
    print(f'Відредактоване повідомлення ---> {res}')


if __name__ == "__main__":
    main()