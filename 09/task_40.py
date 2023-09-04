import os
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
table_path = os.path.join(base_dir, "california_housing_train.csv")

df = pd.read_csv(table_path)

tmp_df = df.loc[(df["population"] <= 500) & (df["population"] >= 0)]

print("Average cost of a house: {}".format(tmp_df["median_house_value"].mean()))