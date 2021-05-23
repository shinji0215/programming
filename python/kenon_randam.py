import datetime
import random

today = datetime.date.today()
print(f'今日は{today}です')

#36.0-36.8までの体温
for i in range(14):
    taion_day = datetime.timedelta(days=i-13)
    r = random.randint(0, 7)

    print(f'{today+taion_day} : {36.0+r*0.1}')

