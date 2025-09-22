import os
import joblib

class Model:
    def __init__(self, model_path=None):
        if model_path is None:
            model_path = os.path.join("artifacts", "model.pkl")
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        self.model, self.train_columns = joblib.load(model_path)

    def predict(self, df):
        # Добавляем недостающие колонки
        missing_cols = set(self.train_columns) - set(df.columns)
        for col in missing_cols:
            df[col] = 0
        df = df[self.train_columns]
        return self.model.predict(df)
