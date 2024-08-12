import pandas as pd
from src.codeforces import until,caculate

data = until.get_data()
data = caculate.slove(data)

df = pd.DataFrame(data)
df.to_excel("ratings.xlsx", index=False)
