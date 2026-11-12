import pandas as pd


def check_semantic_type(column_name, series):
    """
    check the likely business meaning of a column.
    """

    name = column_name.lower()

    if name.endswith("id"): return "identifier"

    if any(word in name for word in [ "charge", "amount", "price", "cost", "revenue"]):
        return "money_valaue"

    if any(word in name for word in ["date", "timestamp", "datetime"]):
        return "date"

    if any(word in name for word in ["tenure", "duration", "period"]):
        return "duration"

    if any(word in name for word in ["churn", "active"]):
        return "boolean"

    if pd.api.types.is_numeric_dtype(series):
        return "numeric"

    if series.nunique(dropna=True) <= 20:
        return "categorical"

    return "text"


def discover_metadata(df):
    """
    Discover technical and semantic metadata
    for every dataset column.
    """

    metadata = []

    for column in df.columns:
        series = df[column]
        metadata.append({
            "column_name": str(column),
            "technical_type": str(series.dtype),
            "semantic_type": check_semantic_type(str(column), series),
            "nullable": bool(series.isna().any()),
            "missing_count": int(series.isna().sum()),
            "unique_count": int(series.nunique(dropna=True)),
            "unique_ratio": round(series.nunique(dropna=True) / len(df), 4)
        })

    return metadata
