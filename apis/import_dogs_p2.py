import requests
import pandas as pd 

r = requests.get("https://api.thedogapi.com/v1/breeds")

# print(r.status_code)

data = r.json()

df = pd.DataFrame(data)
# print(df)

adj = df[["id","name","temperament"]]
print(adj)