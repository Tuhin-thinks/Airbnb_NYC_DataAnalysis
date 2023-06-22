from pathlib import Path

import pandas as pd

TMP_WRITE_DIR = Path(Path(__file__).parent / 'tmp')
TMP_WRITE_DIR.mkdir(exist_ok=True)


def export_as_csv(df: pd.DataFrame, filename: str):
    """
    Function to export a dataframe as a csv file
    
    :param df: DataFrame to export.
    :param filename: export filename.
    :return: Returns the path of the written file.
    """

    write_path = TMP_WRITE_DIR / filename
    df.to_csv(write_path, index=False)
    return write_path
