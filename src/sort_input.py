from pathlib import Path
import pandas as pd

def sort_excel_by_lastname_and_id(excel_path: Path, config: dict) -> None:
    """
    Sorts the Excel file by Last Name, then Unique ID,
    overwriting the file in place.

    :param excel_path: Path to the Excel file to sort
    :param config: Dictionary containing column names
    """
    df = pd.read_excel(excel_path)

    # Columns to sort by
    sort_cols = []
    ascending = []
    if config.get("last_name_column") in df.columns:
        sort_cols.append(config["last_name_column"])
    if config.get("unique_id_column") in df.columns:
        sort_cols.append(config["unique_id_column"])
    if config.get("effective_date_column") in df.columns:
        sort_cols.append(config["effective_date_column"])
        ascending.append(True)

    # Only sort if at least one column exists
    if sort_cols:
        df.sort_values(sort_cols, inplace=True)

    df.to_excel(excel_path, index=False)