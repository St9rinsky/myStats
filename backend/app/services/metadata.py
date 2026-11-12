import pandas as pd


def classify_semantic_type(column_name, series):
    """
    classify the likely business meaning of a column.
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


def determine_analytics_role(semantic_type, series):
    """
    Determine the likely analytics role of a dataset.
    """
    if semantic_type == "identifier": return "identifier"
    if semantic_type == "boolean_or_outcome": return "outcome"
    if semantic_type == "date": return "temporal_dimension"
    if semantic_type == "categorical": return "dimension"

    if semantic_type in ["monetary", "duration", "numeric"]:
        if series.nunique(dropna=True) <= 10:
            return "dimension"

        return "measure"

    if semantic_type == "text": return "descriptive_attribute"
    return "unknown"


def discover_metadata(df):
    """
    Discover technical and semantic metadata
    for every dataset column.
    """

    metadata = []
    total_rows = len(df)

    for column in df.columns:
        series = df[column]
        semantic_type = classify_semantic_type(str(column), series)
        missing_count = int(series.isna().sum())
        unique_count = int(series.nunique(dropna=True))
        

        metadata.append({
            "column_name": str(column),
            "technical_type": str(series.dtype),
            "semantic_type": semantic_type,
            "analytical_role": determine_analytics_role(semantic_type, series),
            "nullable": missing_count > 0,
            "missing_count": missing_count,
            "unique_count": unique_count,
            "unique_ratio": round(unique_count / total_rows, 4)
        })

    return metadata
