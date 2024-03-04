# Словарний индекс
import Perfect_text

def Dict_index():
    s=Perfect_text.get_perfect_text_on_puti('gl9/gl9_zd10.txt')
    s_set=set(s)
    res_dict={}
    for el in s_set:
        res_dict[el]=[]
    file=open('gl9/gl9_zd10.txt','r')
    
    count_line=1
    for line in file:
        line=Perfect_text.get_perfect_text_on_line(line)
        for key, val in res_dict.items():
            if key in line:
                temp=val
                temp.append(count_line)
                res_dict[key]=temp
        count_line+=1
    file.close()
    file=open('gl9/gl9_zd10_res.txt','w')
    for key, val in res_dict.items():
        val=str(val)
        val=val.strip('[')
        val=val.strip(']')
        file.write(f'{key} : {val}\n')
    file.close()


def main():
    Dict_index()


if __name__=='__main__':
    main()