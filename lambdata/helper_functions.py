import pandas as pd
import numpy as np
import sklearn


df = pd.DataFrame()


def null_count(df):
    return df.isnull().sum().sum()

df = pd.DataFrame()


def randomize(df, seed=101):

    df = df.sample(frac=1, random_state=seed)

    return df

class DataFrameHelper:
    def __init__(self, df):
        self.df=df
        self.seed = 43
    def null_count(self):
        count = self.df.isnull().sum().sum()
        return count

    def randomize(self):
        new_df = df.sample(frac =1, random_state =seed)
        return new_df


def train_test_split(df, frac=0.34, seed=73):
    pass