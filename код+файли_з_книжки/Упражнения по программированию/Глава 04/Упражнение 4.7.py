# Упражнение по программированию 4.7

# Мелкая монета для зарплаты

# Объявить переменные для количества копеек в день,
# количества дней и общего количества копеек.
dayPennies = 1 
numDays = 0
total = 0.0

# Получить от пользователей количество дней.
numDays = int(input('Введите количество дней: '))

# Показать таблицу с заработной платой за каждый день.
print ('День\tРубли')
print ('-------------------------')

for day in range(1, numDays + 1):
    print(day, '\t\t', float(dayPennies / 100))
    total += dayPennies
    dayPennies *= 2

# Показать общую заработную плату.
print('Общая заработная плата за', numDays, \
      'дней составит: ',float(total/100), 'рублей')