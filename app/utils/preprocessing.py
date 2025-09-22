import pandas as pd

def preprocess_data(df: pd.DataFrame, train_columns: list) -> pd.DataFrame:
    """
    Подготовка данных как в ноутбуке:
    - OneHotEncoding для Gender
    - заполнение пропусков -1
    - упорядочивание колонок
    """

    if "Gender" in df.columns:
        df = pd.get_dummies(df, columns=["Gender"], drop_first=True)

    df.fillna(-1, inplace=True)

    df = df[train_columns]

    return df
