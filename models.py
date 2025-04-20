# models.py

import joblib


def load_model(
    model_path=(
        r'C:\Users\satya\EmailClassifierProject\email-classification'
        r'\saved_models\classifier_model.pkl'
    )
):
    model = joblib.load(model_path)
    return model
