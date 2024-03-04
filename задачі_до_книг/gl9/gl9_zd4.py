# Унікальні слова
import Perfect_text

def print_unique_words():
    text=Perfect_text.get_perfect_text('gl9/gl9_zd4_text.txt')

    res=set()
    for word in text:
        if text.count(word)==1:res.add(word)
    print(f'Унікальні слова в тексті: {res}')
    
    
def get_unique_words(puti):
    text=Perfect_text.get_perfect_text(puti)

    res=set()
    for word in text:
        if text.count(word)==1:res.add(word)
    return res


def main():
    print_unique_words()


if __name__=='__main__':
    main()