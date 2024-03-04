# Очко
import random as r

def black_jack():
    deck_of_cards = { 'Двійка чірви':2, 'Трійка чірви':3, 'Четвірка чірви':4, 'Пятірка чірви':5, 'Шестірка чірви':6, 'Сімірка чірви':7, 'Вісьмірка чірви':8
                     , 'Девятка чірви':9, 'Десятка чірви':10, 'Валет чірви':1, 'Дама чірви':2, 'Король чірви':3, 'Туз чірви':11,'Двійка піки':2
                     , 'Трійка піки':3, 'Четвірка піки':4, 'Пятірка піки':5, 'Шестірка піки':6, 'Сімірка піки':7, 'Вісьмірка піки':8, 'Девятка піки':9
                     , 'Десятка піки':10, 'Валет піки':1, 'Дама піки':2, 'Король піки':3, 'Туз піки':11,'Двійка буби':2, 'Трійка буби':3, 'Четвірка буби':4
                     , 'Пятірка буби':5, 'Шестірка буби':6, 'Сімірка буби':7, 'Вісьмірка буби':8, 'Девятка буби':9, 'Десятка буби':10, 'Валет буби':1
                     , 'Дама буби':2, 'Король буби':3, 'Туз буби':11, 'Двійка хрісти':2, 'Трійка хрісти':3, 'Четвірка хрісти':4, 'Пятірка хрісти':5, 'Шестірка хрісти':6
                     , 'Сімірка хрісти':7, 'Вісьмірка хрісти':8, 'Девятка хрісти':9, 'Десятка хрісти':10, 'Валет хрісти':1, 'Дама хрісти':2, 'Король хрісти':3
                     , 'Туз хрісти':11 }
    
    player1_score=0
    on_hand_player1=''
    player1_flag=False
    player2_score=0
    player2_flag=False
    on_hand_player2=''
    flag_rozdacha_player1=True
    flag_rozdacha_player2=True
    
    while player1_flag!=True or player2_flag!=True:
        if flag_rozdacha_player1:
            print('\nРоздаємо карти Гравцю1...\n')
            temporary_list=list(deck_of_cards.keys())
            temp=r.choice(temporary_list)
            on_hand_player1+=temp+', '
            player1_score+=deck_of_cards.get(temp)
            #print(player1_score)
            deck_of_cards.pop(temp)
            flag_rozdacha_player1=False
            
        if player1_flag==False:
            print(f'---Гравець1---\nНа руці: {on_hand_player1}\n1.Взяти карту\n2.Зупинитись')
            choice=int(input('Ваш вибір: '))
            
            if choice==1:
                print(f'\nБеремо карту...\n')
                temporary_list=list(deck_of_cards.keys())
                temp=r.choice(temporary_list)
                on_hand_player1+=temp+', '
                player1_score+=deck_of_cards.get(temp)
                #print(player1_score)
                deck_of_cards.pop(temp)
                print(f'----> На руці: {on_hand_player1}\n')
                if player1_score>21:
                    print('Гравець1 набрав більше 21, переміг Гравець2')
                    break
            
            if choice==2:
                player1_flag=True
            
            print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            ok=str(input('Введіть любу клавішу з клавіатури щоб продовжити... '))
                
                
        if flag_rozdacha_player2:
            print('\nРоздаємо карти Гравцю2...\n')
            temporary_list=list(deck_of_cards.keys())
            temp=r.choice(temporary_list)
            on_hand_player2+=temp+', '
            player2_score+=deck_of_cards.get(temp)
            #print(player1_score)
            deck_of_cards.pop(temp)
            flag_rozdacha_player2=False
            
        if player2_flag==False:
            print(f'---Гравець2---\nНа руці: {on_hand_player2}\n1.Взяти карту\n2.Зупинитись')
            choice=int(input('Ваш вибір: '))
            
            if choice==1:
                print(f'\nБеремо карту...\n')
                temporary_list=list(deck_of_cards.keys())
                temp=r.choice(temporary_list)
                on_hand_player2+=temp+', '
                player2_score+=deck_of_cards.get(temp)
                #print(player1_score)
                deck_of_cards.pop(temp)
                print(f'----> На руці: {on_hand_player2}\n')
                if player2_score>21:
                    print('Гравець2 набрав більше 21, переміг Гравець1')
                    break
            
            if choice==2:
                player2_flag=True
                
            print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            ok=str(input('Введіть любу клавішу з клавіатури щоб продовжити... '))
            
    if player1_flag and player2_flag:
        if player1_score>player2_score:
            print(f'Переміг Гравець1 з результатом {player1_score}\nНа його руці: {on_hand_player1}')
        if player2_score>player1_score:
            print(f'Переміг Гравець2 з результатом {player2_score}\nНа його руці: {on_hand_player2}')
        if player2_score==player1_score:
            print(f'Нічья в Гравця1 {player1_score} а в Гравця2 {player2_score}\nНа руках у Гравця1 {on_hand_player1}\nНа руках у Гравця2 {on_hand_player2}')
                
            

def main():
    black_jack()


if __name__=='__main__':
    main()