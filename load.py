import pandas as pd
import sqlite3

def load(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"Data berhasil disimpan ke {output_file}")

def load_to_sqlite(df,db_file, table_name):
    conn = sqlite3.connect(db_file)
    df.to_sql(table_name, conn, if_exists="replace",index=False)
    conn.close()
    print(f"Data berhasil disimpan di dalam database bernama {db_file}")

if __name__ == "__main__":
    df = pd.read_csv("Indonesia_Financial.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.dropna()
    load(df, "indonesia_financial.csv")
    load_to_sqlite(df, "indonesia_financial.db", "financial_data")

