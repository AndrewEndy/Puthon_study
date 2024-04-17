# Рекурсивная сумма списка


def func(n_list):
    n=len(n_list)
    if n_list!=[]:
        return n_list[-1] + func(n_list[0:n-1])
    else:return 0




def main():
    n_list=[]
    for i in range(5):
        i=int(input(': '))
        n_list.append(i)
    sum=func(n_list)
    print(sum)
    
    
    
if __name__=='__main__':
    main()