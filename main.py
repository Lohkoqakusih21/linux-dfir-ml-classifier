import argparse
from src.pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser(description="DFIR ML Classifier")
    parser.add_argument("--path", required=True, help="Target directory")
    args = parser.parse_args()

    result = run_pipeline(args.path)

    print(result.head())
    result.to_csv("output.csv", index=False)


if __name__ == "__main__":
    main()