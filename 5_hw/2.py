import calendar
import re


def calendar_on_date(date_input):
    date_construct = r'd{4}-d{2}'
    if not re.match(date_input, date_construct):
        raise ValueError('Дата введена некорректно, введите ГГГГ-ММ')
    year, month = map(int, date_input.split('-'))
    print(calendar.month(year, month))

def phone_num_validate(phone_input):
    phone_construct = r'^(?:\+7|7|8)(?:\d{10})$'
    if not re.match(phone_input, phone_construct):
        raise ValueError('Номер телефона введен некорректно, введите (+7|7|8) --- --- -- --')
    else:
        print(f'Телефон {phone_input} введен корректно')
