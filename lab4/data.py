#1 Напишите программу на Python для вычитания пяти дней из Японии.

#2 Напишите программу Python для печати вчера, сегодня, завтра.

#3 Напишите программу на Python, чтобы отбрасывать микросекунды из дат и времени.

#4 Напишите программу на Python для изучения разницы между двумя датами в секундах.


from datetime import datetime, timedelta

# #1


# now_day = datetime.now()
# back5 = now_day - timedelta(days=5)
# print("\n сегодня:", now_day,"\n")
# print("5 дней назад:", back5)


# #2


# today = datetime.now().date()
# yesterday = today - timedelta(days=1)
# tomorrow = today + timedelta(days=1)

# print("\nвчера ", yesterday)
# print("сегодея ", today)
# print("завтра ", tomorrow,'\n')


# #3

# now = datetime.now()
# microsec = now.replace(microsecond=0)
# print("\nсейчас", now)
# print("без микросекунд", microsec,'\n')


# #4

date1 = datetime(2023, 2, 20, 12, 0, 0)
date2 = datetime(2023, 2, 20, 12, 0, 12)
date3 = datetime(2023, 2, 20, 12, 1, 40)

dif1 = (date2 - date1).total_seconds()
dif2 = (date3 - date1).total_seconds()
print("\nразница в секундах", dif1)
print("разница в секундах", dif2,'\n')

