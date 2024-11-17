import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie", "David"],
       "Age": [24, 27, 22, 32],
       "City": ["New York", "Los Angeles", "Chicago", "Houseton"]
       }

df = pd.DataFrame(data)

df.head(3)

df = df.replace("Alice", "Alice Smith")

