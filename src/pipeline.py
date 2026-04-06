import pandas as pd
from tqdm import tqdm

from src.acquisition import scan_directory
from src.feature_extraction import extract_features
from src.model import load_model, predict


def run_pipeline(path):
    files = scan_directory(path)

    data = []
    for f in tqdm(files, desc="Extracting features"):
        feat = extract_features(f)
        if feat:
            data.append(feat)

    df = pd.DataFrame(data)

    model = load_model()
    result = predict(model, df)

    return result