from collections import Counter
import os

import pandas as pd
from pandas import DataFrame

from db_parse_config import db_file, quarters, products

def db_parse(df, companies, periods, products):
    results_list = []

    for product in products:
        for period in periods:
            for company in companies:
                result_series = df[(
                    df.delivery_date >= periods[period][0]) & (
                    df.delivery_date <= periods[period][1]) & (
                    df.company == company)
                ][products[product]].sum()

                if result_series.values.any():
                    results_list.append([product, company, result_series.sum(), period])
    
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
    _, ext = os.path.splitext(db_file)
    if ext in ['.xls', '.xlsx']:
        df = pd.read_excel(db_file)
    elif ext in ['.csv']:
        df = pd.reas_csv(db_file)
    else:
        print('Ошибка чтения файла с базой данных!')
        raise OSError

    # Читаем .xlsx файл в DataFrame
    

    # Заменим все NaN в данных на нули
    df = df.fillna(0)

    # Получим массив компаний
    companies = list(Counter(df.company).keys())

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


