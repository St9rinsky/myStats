
import pandas as pd


def get_overview(df: pd.DataFrame):
    """
    Generate a general overview of a dataset.
    """

    overview = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()), #dup rows
        "total_missing_values": int(df.isna().sum().sum()), #missing values
        "columns_with_missing_values": {},
        "numeric_summary": {}
    }

    missing_values = df.isna().sum()

    for column, count in missing_values.items():
        if count > 0:
            overview["columns_with_missing_values"][column] = int(count)

    numeric_columns = df.select_dtypes(include="number")

    for column in numeric_columns.columns:

        series = numeric_columns[column].dropna()

        if series.empty:
            continue

        overview["numeric_summary"][column] = {
            "mean": float(series.mean()),
            "median": float(series.median()),
            "minimum": float(series.min()),
            "maximum": float(series.max()),
            "standard_deviation": (
                float(series.std()) if len(series) > 1 else None
            )
        }

    return overview



def group_by( df: pd.DataFrame, group_column: str, aggregation_column: str | None = None, operation: str = "count"):
    """
    Group dataset df by group column and perform aggregations calculations based on the agregation column and operation specified

    ARGs
    - df: pd.DataFrame - The dataset to be grouped
    - group_column: str - The column to group by
    - aggregation_column: str | None - The column to perform aggregation on (optional)
    - operation: str - The aggregation operation to perform (default: "count")

    EXAMPLE
    Group a dataset by country and calculate the count of rows in each group
    """

    # non existant column in dataframe
    if group_column not in df.columns:
        raise ValueError(f"Column '{group_column}' does not exist")

    # if the aggregation column is given but does not exist in the dataframe
    if aggregation_column is not None and aggregation_column not in df.columns:
        raise ValueError(f"Column '{aggregation_column}' does not exist")

    # surported operations
    allowed_operations = {
        "count", "sum", "mean", "median", "min", "max", "nunique"
    }
    if operation not in allowed_operations:
        raise ValueError(f"Unsupported operation: {operation}")

    grouped = df.groupby(group_column, dropna=False)

    # Perform aggregation
    if aggregation_column is None:
        if operation != "count":
            raise ValueError("An aggregation column is required for this operation")

        #get the count of rows in each group
        result = grouped.size()

    else:
        result = grouped[aggregation_column].agg(operation)

    results = []

    for group_value, aggregate_value in result.items():

        if pd.isna(group_value): group_value = None
        elif hasattr(group_value, "item"): group_value = group_value.item()

        if pd.isna(aggregate_value): aggregate_value = None
        elif hasattr(aggregate_value, "item"): aggregate_value = aggregate_value.item()

        results.append({group_column: group_value, "value": aggregate_value})

    return {
        "group_column": group_column,
        "aggregation_column": aggregation_column,
        "operation": operation,
        "results": results
    }
