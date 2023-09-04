import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
#print(data)

oh_data = pd.DataFrame()

unique_data = data['whoAmI'].unique()

for val in unique_data:
    oh_data[val] = (data['whoAmI'] == val).astype(int)

print(oh_data)