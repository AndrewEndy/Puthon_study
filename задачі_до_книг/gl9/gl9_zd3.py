# Шифрування і дешифрування

def encrypt_the_file():
    file = open('gl9/Deciphered.txt','r',encoding='utf-8')
    s=file.read()
    file.close()
    cipher = { 'А':'"', 'Б':'№', 'В':'₴', 'Г':'!', 'Д':';', 'Е':'%', 'Є':':', 'Ж':'?', 'З':'*', 'И':'(', 'І':')', 'Ї':'_', 'Й':'+', 'К':'@', 'Л':'#', 'М':'$', 'Н':'^'
            , 'О':'&', 'П':'~', 'Р':'`', 'С':'-', 'Т':'=', 'У':'/', 'Ф':'.', 'Х':'>', 'Ц':',', 'Ч':'<', 'Ш':'}', 'Щ':'{', 'Ь':']', 'Ю':'[', 'Я':':'}

    file2=open('gl9/Ciphered.txt','w',encoding='utf-8')
    for word in s.upper():
        if cipher.get(word,'None')=='None':
            file2.write(word)
        else:
            file2.write(cipher[word])
    file2.close()


def decrypt_the_file():
    file = open('gl9/Ciphered.txt','r',encoding='utf-8')
    s=file.read()
    file.close()      
    cipher = { 'А':'"', 'Б':'№', 'В':'₴', 'Г':'!', 'Д':';', 'Е':'%', 'Є':':', 'Ж':'?', 'З':'*', 'И':'(', 'І':')', 'Ї':'_', 'Й':'+', 'К':'@', 'Л':'#', 'М':'$', 'Н':'^'
            , 'О':'&', 'П':'~', 'Р':'`', 'С':'-', 'Т':'=', 'У':'/', 'Ф':'.', 'Х':'>', 'Ц':',', 'Ч':'<', 'Ш':'}', 'Щ':'{', 'Ь':']', 'Ю':'[', 'Я':':'}
    deciphered={}
    for key,value in cipher.items():
        deciphered[value]=key

    file2=open('gl9/Deciphered.txt','w',encoding='utf-8')
    for word in s:
        if deciphered.get(word,'None')=='None':
            file2.write(word)
        else:
            file2.write(deciphered[word])
    file2.close()


def main():
    decrypt_the_file()


if __name__=='__main__':
    main()