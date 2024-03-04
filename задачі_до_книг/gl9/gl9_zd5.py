# Частота слів
import Perfect_text


def frequency_of_words():
    text = Perfect_text.get_perfect_text('gl9/gl9_zd4_text.txt')
    
    text_set=set(text)
    text_dict={}
    for word in text_set:
        count=text.count(word)
        text_dict[word]=count

    file = open('gl9/gl9_zd5_res.txt','w')
    for key, val in text_dict.items():
        file.write(f'{key} ---> {val}\n')
    file.close()

def main():
    frequency_of_words()


if __name__=='__main__':
    main()