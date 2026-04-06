import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

MODEL_PATH = "models/model.pkl"

def train_model(df):
    X = df[["size", "entropy"]]
    y = df["label"]

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    return model


def load_model():
    return joblib.load(MODEL_PATH)


def predict(model, df):
    X = df[["size", "entropy"]]
    df["prediction"] = model.predict(X)
    return df