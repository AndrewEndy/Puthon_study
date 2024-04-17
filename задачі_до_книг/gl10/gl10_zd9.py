# Викторина

class Question:
    def __init__(self,question,answer1,answer2,answer3,answer4,right_answer) -> None:
        self.__question=question
        self.__answer1=answer1
        self.__answer2=answer2
        self.__answer3=answer3
        self.__answer4=answer4
        self.__right_answer=right_answer
        
        
    def __str__(self) -> str:
        return f'\n{self.__question}' + \
            f'\n1.{self.__answer1}' + \
            f'\n2.{self.__answer2}' + \
            f'\n3.{self.__answer3}' + \
            f'\n4.{self.__answer4}'
    
    def get_right_answer(self):
        return self.__right_answer
    
    def get_answer(self):
        print(self)
        choice=int(input('Вибір: '))
        if choice==self.__right_answer:return 1
        else:return 0
            

def create_question():
    player2_question=[]
    for question in range(5):
        print()
        question_wop=str(input('Введіть ваше питання: '))
        answer1=str(input('Варіант відповіді 1: '))
        answer2=str(input('Варіант відповіді 2: '))
        answer3=str(input('Варіант відповіді 3: '))
        answer4=str(input('Варіант відповіді 4: '))
        right_answer=int(input('Парвильний варіант відповіді (типу перший-1 і тп): '))
        question=Question(question_wop,answer1,answer2,answer3,answer4,right_answer)
        player2_question.append(question)
    return player2_question


def get_answer(player1_question):
    count=0
    for question in player1_question:
        count+=question.get_answer()
    return count
        

def main():
    player1_question=[]
    question1=Question('Хто напав на Польщу?','Гітлер','Сталін','Гітлер і Сталін','Порошенко',3)
    question2=Question('Хто домбив бомбас?','Гітлер','Зеленський','Укронацисти','Порошенко',3)
    question3=Question('ХТО ПІДАРАС?','Саня','Андрій','Кабан','Тоха',3)
    question4=Question('Хто какашка?','Саня','Андрій','Кабан','Тоха',4)
    question5=Question('Хто красавчик?','Саня','Андрій','Кабан','Тоха',2)
    player1_question.append(question1)
    player1_question.append(question2)
    player1_question.append(question3)
    player1_question.append(question4)
    player1_question.append(question5)
    
    player2_question=create_question()
    
    player1_count=get_answer(player1_question)
    player2_count=get_answer(player2_question)
    print(f'\nГравець 1 набрав: {player1_count} правильних відповідей ----- Гравець 2 набрав: {player2_count} правильних відповідей')
    
    
    


if __name__=='__main__':
    main()