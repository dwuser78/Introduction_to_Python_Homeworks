import os
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
table_path = os.path.join(base_dir, "california_housing_train.csv")

df = pd.read_csv(table_path)

tmp_df = df.groupby("households")["population"].min()

print("Maximum 'households' for minimum 'population': {}" \
      .format(tmp_df.index[tmp_df.count() - 1]))