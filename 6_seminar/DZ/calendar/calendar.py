
MOUNTHS_DAYS = {"Январь":31,"Февраль":[28, 29],"Март":31,"Апрель":30,"Май":31,"Июнь":30,"Июль":31,"Август":31, \
        "Сентябрь":30,"Октябрь":31,"Ноябрь":30,"Декабрь":31}
MOUNTHS = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август", \
        "Сентябрь","Октябрь","Ноябрь","Декабрь"]

def calendar_check(date_):
    days_count = 0
    day, mounth, year, *args = [int(x) for x in date_.split(".")]

    if year < 1 or year > 9999:
        return False
    
    if mounth < 1 or mounth > 12:
        return False


    if mounth != 2:
        days_count = MOUNTHS_DAYS[MOUNTHS[mounth-1]]
    else:
        not_leap_mounth, leap_mounth = MOUNTHS_DAYS[MOUNTHS[mounth-1]]
        
        if _is_leap(year):
            days_count = leap_mounth
        else:
            days_count = not_leap_mounth
    
    if day < 1 or day > days_count:
        return False
    
    return True


def _is_leap(year):

    if year % 400 == 0:
        return True
    
    if year % 100 == 0:
        return False
    
    if year % 4 ==0:
        return True
    
    return False
