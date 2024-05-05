week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
dict_week = {key:value for key, value in zip(week_days, [n for n in range(1,8)])}
print(dict_week)