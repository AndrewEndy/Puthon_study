# Середння кількість слів

def average_number_of_words():
    file=open('gl8_zd6.txt','r',encoding='utf-8')
    s=file.read()
    file.close()
    return len(s.split()),len(s.split())/len(s.split('.')),len(s.split('.'))


def main():
    res=average_number_of_words()
    print(f'''Кількість слів ---> {res[0]}\nСередня кількість слів ---> {res[1]}\nКількість речень ---> {res[2]} ''')


if __name__ == "__main__":
    main()