# Інформація про навчальні курси

def info_about_course():
    num_of_class = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'CS104':'1244', 'CS105':'1411' }
    teacher_dict = {'CS101':'Хайнс', 'CS102':'Альварадо', 'CS103':'Рич', 'NT110':'Берк', 'CM241':'Ли' }
    time_of_class = {'CS101':'8:00', 'CS102':'9:00', 'CS103':'10:00', 'NT110':'11:00', 'CM241':'13:00' }
    
    num_of_course=str(input('Введіть номер курсу: '))
    print('Номер аудиторії: ' + num_of_class.get(num_of_course,'None'))
    print('Вчитель: ' + teacher_dict.get(num_of_course,'None'))
    print('Час: ' + time_of_class.get(num_of_course,'None'))

def main():
    info_about_course()


if __name__=='__main__':
    main()