import pandas as pd

from collections import Counter

# Читаем .xlsx файл в DataFrame
df = pd.read_excel('bd.xlsx')

# Заменим все NaN в данных на нули
df = df.fillna(0)

# Получим массив компаний
companies = list(Counter(df.company).keys())

# Предварительный массив продуктов
products = list(df.columns[2:-9])

year = '2018'

periods = {
    f'1кв. {year}г.': [f'{year}-01-01', f'{year}-03-31'],
    f'2кв. {year}г.': [f'{year}-04-01', f'{year}-06-30'],
    f'3кв. {year}г.': [f'{year}-07-01', f'{year}-09-30'],
    f'4кв. {year}г.': [f'{year}-10-01', f'{year}-12-31'],
}

print(periods)


# periods = ['2008-01-01', '2008-04-01', '2008-07-01', '2008-10-01','2009-01-01']


# df[
#     (df.delivery_date > '2008-09-09') &
#     (df.delivery_date <= '2009-09-09') &
#     (df.company == companies[1])][['company', products[1]]]

prod = '1892ВМ14Я('

product = list(filter(lambda x: '1892ВМ14Я(' in x, products))

for company in companies:
    for quarter in periods:
        # print(quarter, f'c {periods[quarter][0]} по {periods[quarter][1]}')
        if df[(
                df.delivery_date >= periods[quarter][0]) & (
                df.delivery_date <= periods[quarter][1]) & (
                df.company == company)
                ][product].sum().values.any():

            print(f'Компания - {company}')
            print(f'за {quarter}')
            
            print(df[(
                df.delivery_date >= periods[quarter][0]) & (
                df.delivery_date <= periods[quarter][1]) & (
                df.company == company)][product].sum())


# for product in products:
#     for company in companies:
#         for i in range(len(periods)-2):
#             if df[(df.delivery_date > periods[i]) & (df.delivery_date <= periods[i+1]) & (df.company == company)][[product]].sum().values[0]:
#                 print(f'Компания - {company}')
#                 print(f'за {periods_kirilic[i+1]}')
#                 print(df[(df.delivery_date > periods[i]) & (
#                     df.delivery_date <= periods[i+1]) & (df.company == company)][[product]].sum())

# pd.Series.sum()
