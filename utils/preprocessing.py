import numpy as np
import pandas as pd

IRRELEVANT_COLS = [
    'name', 'host_name'
]


def find_missing_data_freq(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to read the dataframe and find the missing data per column
    
    :param df: Input dataframe to look for missing data.
    :return: A dataframe with the missing data frequency per column
    """
    # find the count of missing data per column
    missing_data = df.isna().sum()
    missing_data_percent = 100 * missing_data / len(df)
    missing_data_table = pd.concat([missing_data, missing_data_percent], axis=1)
    missing_data_table = missing_data_table.rename(
        columns={0: "Missing Data", 1: "% of Missing Data"}
    )
    missing_data_table = missing_data_table[
        missing_data_table.iloc[:, 1] != 0
    ].sort_values("% of Missing Data", ascending=False).round(2)
    return missing_data_table


def drop_irrelevant_cols(df0: pd.DataFrame):
    """
    Function to drop irrelevant columns from the dataframe (inplace)
    
    :param df0: Input dataframe to drop irrelevant columns from
    :return: None
    """
    df0.drop(IRRELEVANT_COLS, axis=1, inplace=True)
