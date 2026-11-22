import pandas as pd

from app.services.compute import get_overview , group_by, filter_data


df = pd.DataFrame({
    "customer": ["A", "B", "C", "C"],
    "tenure": [10, 20, 30, 30],
    "charges": [100.0, 200.0, 300.0, 300.0],
    "contract": ["Monthly", "Yearly", "Monthly", "Monthly"]
})

result = get_overview(df)

print(result)



df = pd.DataFrame({
    "customerID": ["1", "2", "3", "4"],
    "MonthlyCharges": [50, 120, 90, 150]
})

result = filter_data(
    df=df,
    column="MonthlyCharges",
    operator=">",
    value=100
)

print(result)
