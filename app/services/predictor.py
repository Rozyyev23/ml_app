from app.utils.preprocessing import preprocess_data

class Predictor:
    def __init__(self, model):
        self.model = model

    def predict(self, df):
        processed_df = preprocess_data(df, self.model.train_columns)
        return self.model.predict(processed_df)
