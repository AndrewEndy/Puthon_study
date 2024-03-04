# Прінтер дат


def date_calculation(date):
    months={'01':'січеня', '02':'лютого', '03':'березня', '04':'квітеня', '05':'травеня', '06':'червня', 
            '07':'липня', '08':'серпня', '09':'вересня', '10':'жовтня', '11':'листопада', '12':'грудня'}
    
    date_list=date.split(date[2])
    month=''
    bool_month=False
    for key in months.keys():
        if key==date_list[1]:
            bool_month=True
            month=months.get(key)
            if key=='02' and int(date_list[0])>28 and int(date_list[2])%4!=0:
                return 'Ви ввели невірний день'
            elif key=='02' and int(date_list[0])>29 and int(date_list[2])%4==0:
                return 'Ви ввели невірний день'
            elif (key=='01' or key=='03' or key=='05' or key=='07' or key=='08' or key=='10' or key=='12') and int(date_list[0])>31:
                return  'Ви ввели невірний день'
            elif (key=='04' or key=='06' or key=='09' or key=='11') and int(date_list[0])>30: 
                return  'Ви ввели невірний день'
    if bool_month==False:
        return 'Ви вказали неправильний місяць'
    return f'{date_list[0]} {month} {date_list[2]} року'
            


def main():
    date=str(input('Введіть дату: '))
    res=date_calculation(date)
    print(res)
    

if __name__ == "__main__":
    main()