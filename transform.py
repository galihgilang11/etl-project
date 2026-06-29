import pandas as pd

def transform (df):
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.dropna()
    return df

if __name__ == "__main__":
    df = pd.read_csv("Indonesia_Financial.csv")
    df_bersih = transform(df)
    print(df_bersih.shape)
    print(df_bersih.head().to_string())
    print(df_bersih.dtypes)
