import pandas as pd

data = {
    "product": ["Laptop", "Monitor", "Keyboard"],
    "sales": [1200, 800, 300]
}

df = pd.DataFrame(data)

df.to_csv("sample_data.csv", index=False)

print("csv creado correctamente")