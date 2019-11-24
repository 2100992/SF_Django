import pandas as pd
from pandas import read_csv

def parse_csv(db, file):
    df = read_csv(file)
    