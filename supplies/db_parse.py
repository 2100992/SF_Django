import pandas as pd
from pandas import DataFrame

from collections import Counter


def db_parse(df, companies, periods, products):
    # print(df)
    # print(companies)
    # print(periods)
    # print(products)

# result_df = DataFrame({'product':[], 'company':[], 'count':[], 'period':[]})
    results_list = []

    for product in products:
        for company in companies:
            for period in periods:
                result_series = df[(
                    df.delivery_date >= periods[period][0]) & (
                    df.delivery_date <= periods[period][1]) & (
                    df.company == company)
                ][products[product]].sum()

                if result_series.values.any():
                    results_list.append([product, company, result_series.sum(), period])
                    # print(
                    #     f'{product} - {company} - {result_series.sum()} - {period}')
    
    result = DataFrame(results_list)

    result.columns = [
        'product',
        'company',
        'count',
        'period',
    ]

    print(result)

    result.to_excel('test1.xlsx', sheet_name='sheet1', index=False)


def init():

    # Читаем .xlsx файл в DataFrame
    # df = pd.read_excel('bd.xlsx')
    df = pd.read_excel('bd.xlsx')

    # Заменим все NaN в данных на нули
    df = df.fillna(0)

    # Получим массив компаний
    companies = list(Counter(df.company).keys())
    # print(companies)

    # Предварительный массив продуктов из файла
    # Подсмотрим и распределим по группам

    # products = list(df.columns[1:-1])
    # print(products)

    # Продукты по группам
    # ToDo вынести в конфигурационный файл
    products = {
        '1892ВМ15Ф': ['1892ВМ15АФ', '1892ВМ15АФ(ОТК)', '1892ВМ15АФ(ВП)'],
        '1892BM12Т': ['1892ВМ12АТ', '1892ВМ12АТ (ГК)', '1892BM12Т(ФК НУ)', '1892BM12Т(ОТК)', '1892BM12АТ(ВП)'],
        '1892ВМ2Я': ['1892ВМ2Т\n("ФК")', '1892ВМ2Я\n(ВП)', '1892ВМ2Т\n(ОТК)', '1892ВМ2Я\n(ОТК)', '1892ВМ2Я\n("ФК")'],
        '1892ВМ10Я': ['1892ВМ10Я\n(ГК)', '1892ВМ10Я(ФК в НУ)', '1892ВМ10Я\n(ОТК)', '1892ВМ10Я\n(ВП)'],
    }

    # Отчетный год
    year = '2019'

    quarters = {
        f'1кв. {year}г.': [f'{year}-01-01', f'{year}-03-31'],
        f'2кв. {year}г.': [f'{year}-04-01', f'{year}-06-30'],
        f'3кв. {year}г.': [f'{year}-07-01', f'{year}-09-30'],
        f'4кв. {year}г.': [f'{year}-10-01', f'{year}-12-31'],
    }

    # print(quarters)

    # Подготовка группы товаров, содержащих в prod
    # prod = 'ча'
    # product = list(filter(lambda x: prod in x, products))

    data = {
        'df': df,
        'companies': companies,
        'periods': quarters,
        'products': products
    }

    return data


if __name__ == "__main__":
    data = init()
    db_parse(data['df'], data['companies'], data['periods'], data['products'])


# for product in products:
#     for company in companies:
#         for i in range(len(periods)-2):
#             if df[(df.delivery_date > periods[i]) & (df.delivery_date <= periods[i+1]) & (df.company == company)][[product]].sum().values[0]:
#                 print(f'Компания - {company}')
#                 print(f'за {periods_kirilic[i+1]}')
#                 print(df[(df.delivery_date > periods[i]) & (
#                     df.delivery_date <= periods[i+1]) & (df.company == company)][[product]].sum())

# pd.Series.sum()
