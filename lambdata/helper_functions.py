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
