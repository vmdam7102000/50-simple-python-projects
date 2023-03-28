import pandas as pd

if __name__ == '__main__':
    df = pd.read_json("input.json")
    df.to_csv("output.csv")