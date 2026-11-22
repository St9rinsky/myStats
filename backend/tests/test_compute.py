import pandas as pd

from app.services.compute import get_overview


df = pd.DataFrame({
    "customer": ["A", "B", "C", "C"],
    "tenure": [10, 20, 30, 30],
    "charges": [100.0, 200.0, 300.0, 300.0],
    "contract": ["Monthly", "Yearly", "Monthly", "Monthly"]
})

result = get_overview(df)

print(result)