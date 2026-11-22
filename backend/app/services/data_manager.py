
from dataclasses import dataclass

import pandas as pd


@dataclass
class ActiveDataset:
    dataframe: pd.DataFrame
    filename: str
    metadata: list[dict]


_active_dataset: ActiveDataset | None = None


def store_dataset(df: pd.DataFrame, filename: str, metadata: list[dict]):
    """
    Store the currently active dataset in memory.
    """
    global _active_dataset

    _active_dataset = ActiveDataset(
        dataframe=df,
        filename=filename,
        metadata=metadata
    )


def get_active_dataset():
    """
    Retrieve the currently active dataset.
    """
    return _active_dataset


def get_dataset_summary():
    """
    Return information about the active dataset.
    """
    if _active_dataset is None:
        return None

    df = _active_dataset.dataframe

    return {
        "filename": _active_dataset.filename,
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "columns": _active_dataset.metadata
    }


def clear_dataset():
    """
    Remove the currently active dataset from memory.
    """
    global _active_dataset

    _active_dataset = None
