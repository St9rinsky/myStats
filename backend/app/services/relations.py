import pandas as pd

def discover_relations(parent_df, child_df, parent_name, child_name):
    """
    Discover relationships between dataset columns.
    """
    relations = []

    for parent_column in parent_df.columns:
        for child_column in child_df.columns:
            if parent_column.lower() != child_column.lower():
                continue

            parent_values = parent_df[parent_column].dropna()
            child_values = child_df[child_column].dropna()

            if parent_values.duplicated().any():
                continue

            if not child_values.isin(parent_values).all():
                continue

            relations.append({
                "parent_dataset": parent_name,
                "parent_column": parent_column,
                "child_dataset": child_name,
                "child_column": child_column,
                "relationship_type": "one_to_many",
                "confidence": "high"
            })
            
    return relations