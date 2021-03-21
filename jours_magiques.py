from datetime import *

len_weekday_name = (5, 5, 8, 5, 8, 6, 8)

day_delta = timedelta(days = 1)

start_date = date(2000, 1, 1)
end_date = date.today()

def magical_days_counter():
    magical_days = []
    for i in range((end_date - start_date).days):
        current_date = start_date + i * day_delta
        current_weekday = current_date.weekday()
        if (int(str(current_date)[8] + str(current_date)[9]) + len_weekday_name[current_weekday]) % 10 == 0:
            magical_days.append(str(current_date))
    return magical_days


print(magical_days_counter())
print(len(magical_days_counter()))