"""
Workshop sample data generation.

"""

import pandas as pd


_FY = [
    {'name': 'Microsoft',
     'year': '2016',
     'count_of_employees': '114'},
    {'name': 'Microsoft',
     'year': '2017',
     'count_of_employees': '124'},
    {'name': 'Microsoft',
     'year': '2018',
     'count_of_employees': '131'},
    {'name': 'Google',
     'year': '2016',
     'count_of_employees': '72'},
    {'name': 'Google',
     'year': '2017',
     'count_of_employees': '74'},
    {'name': 'Google',
     'year': '2018',
     'count_of_employees': '76'}
]

_STOCK = [
    {'tic': 'msft',
     'yr': 2018,
     'price': 86.13},
    {'tic': 'msft',
     'yr': 2017,
     'price': 62.79},
    {'tic': 'msft',
     'yr': 2016,
     'price': 54.32}
]


if __name__ == '__main__':
    pd.DataFrame(_FY).to_stata('../data/firmyear.dta', write_index=False)
    pd.DataFrame(_STOCK).to_csv('../data/stock.csv', index=False)