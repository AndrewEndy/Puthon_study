# Аналіз Файла
import Perfect_text
from gl9_zd4 import get_unique_words

def file_analysis():
    text1=Perfect_text.get_perfect_text('gl9/gl9_zd4_text.txt')
    text1_set=set(text1)
    
    text2=Perfect_text.get_perfect_text('gl9/gl9_zd6_text.txt')
    text2_set=set(text2)
    #print(f'{text1_set}\n\n\n{text2_set}')
    
    file=open('gl9/gl9_zd6_res.txt','w',encoding='utf-8')
    res=get_unique_words('gl9/gl9_zd4_text.txt')
    file.write(f'Унікальні слова в тексті \'gl9/gl9_zd4_text.txt\':\n {res}\n')
    res=get_unique_words('gl9/gl9_zd6_text.txt')
    file.write(f'Унікальні слова в тексті \'gl9/gl9_zd6_text.txt\':\n {res}\n')
    file.write(f'Слова які входять в обидва файли:\n {text1_set | text2_set}\n')
    file.write(f'Слова які входять в файл1 але не входять в файл2:\n {text1_set - text2_set}\n')
    file.write(f'Слова які входять в файл2 але не входять в файл1:\n {text2_set - text1_set}\n')
    file.write(f'Слова які входять або в файл2 або в файл1 але не входять в них двох:\n {text2_set ^ text1_set}\n')

def main():
    file_analysis()


if __name__=='__main__':
    main()