
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
