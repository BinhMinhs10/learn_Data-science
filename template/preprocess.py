import numpy as np


class Preprocess():
    """
    Parameters
    ----------

    time: Dataframe
        data to extract time with the matching url with df

    columns_to_drop: list
        columns to drop in the dataframe

    dropna_columns: list
    """
    def __init__(self):
        self.colummns_to_drop

    @staticmethod
    def extract_emotion(df):
        df.drop('emotion', axis=1, implace=True)
        return df

    def drop_columns(self, df):
        df.drop(self.colummns_to_drop, axis=1, inplace=True)
        return df

    def extract_date_hour_minute(self, string: str):
        try:
            return string[:16]
        except TypeError:
            return np.nan

    def process(self, df):
        df = self.drop_columns(df)
        df = self.extract_emotion(df)
        return df

