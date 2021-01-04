
import datetime
day=datetime.date.today()

dattod= datetime.date(2020,12,31)
datmayday=datetime.date(2021, 1, 25)
print ("Дата ближайшего  моего дня  рождения : ", datmayday)


print("сегодня у меня день рождения ??? ", dattod > datmayday)

print("до моего дня рождения ", (datmayday-dattod).days, "  дней ")

