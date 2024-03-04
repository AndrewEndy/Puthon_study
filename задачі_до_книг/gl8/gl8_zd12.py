# Молодіжний жаргон

def jargon(s):
    s_list=s.split()
    res=''
    
    for word in s_list:
        first_el=word[0]
        word=word[1:]
        res+=word+first_el+'ки '
    return res
        

def main():
    s=str(input('Введіть ваше повідомлення: '))
    res=jargon(s)
    print(f'Повідомлення в молодіжному жаргоні: {res}')
    

if __name__ == "__main__":
    main()