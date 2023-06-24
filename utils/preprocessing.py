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


def find_host_missing_review_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to find the frequency of missing data to non-missing data for each unique hosts and
    the count of missing and non-missing data.
    
    :param df: input dataframe to analyze
    :return: report dataframe with the following columns:
        - host_id: unique host id
        - missing_review_count: count of missing reviews
        - non_missing_review_count: count of non-missing reviews
        - missing_review_percent: percent of missing reviews
    """
    df_report = pd.DataFrame(columns=['host_id', 'missing_review_count', 'non_missing_review_count',
                                      'missing_review_percent'])
    
    df_copy = df.copy()
    # find the count of missing data per column
    df_copy['number_of_reviews'] = df['number_of_reviews'].fillna(0)
    df_copy['last_review'] = pd.to_datetime(df['last_review'])
    df_copy['reviews_per_month'] = df['reviews_per_month'].fillna(0)
    
    # create new columns to find the missing data
    df_report['missing_review_count'] = None
    df_report['non_missing_review_count'] = None
    df_report['missing_review_percent'] = None
    
    for host_id in df_copy['host_id'].unique():
        host_id_filter = df_copy['host_id'] == host_id
        missing_condition = ((df_copy['number_of_reviews'] == 0) | (df_copy['last_review'].isna()) | (
                df_copy['reviews_per_month'] == 0))
        non_missing_condition = ~missing_condition
        
        missing_data_count = df_copy[host_id_filter & missing_condition].shape[0]
        non_missing_data_count = df_copy[host_id_filter & non_missing_condition].shape[0]
        missing_data_percent = 100 * missing_data_count / (missing_data_count + non_missing_data_count)
        
        # add a new row to the report dataframe
        temp_df = pd.DataFrame(
            [[host_id, missing_data_count, non_missing_data_count, missing_data_percent]],
            columns=['host_id', 'missing_review_count',
                     'non_missing_review_count', 'missing_review_percent'])
        
        df_report = pd.concat([df_report, temp_df], ignore_index=True)
    
    return df_report
