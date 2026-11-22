import pandas as pd

from app.services.compute import get_overview , group_by, filter_data, sort_data, add_calculated_column


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
    conditions=[
        {"column": "MonthlyCharges", "operator": ">", "value": 100}
    ],
)

print(result)


# multiple conditions
result = filter_data(
    df=df,
    conditions=[
        {"column": "MonthlyCharges", "operator": ">", "value": 100},
        {"column": "customerID", "operator": "!=", "value": "2"}
    ],
    logic="AND"
)

print(result)


df = pd.DataFrame({
    "customerID": ["1", "2", "3", "4"],
    "MonthlyCharges": [50, 120, 90, 150]
})

result = sort_data(
    df=df,
    column="MonthlyCharges",
    ascending=False
)

print(result)


df = pd.DataFrame({
    "customerID": ["1", "2", "3"],
    "MonthlyCharges": [50, 120, 90]
})

result = add_calculated_column(
    df=df,
    new_column="AnnualCharges",
    source_column="MonthlyCharges",
    operation="multiply",
    value=12
)

print(result)