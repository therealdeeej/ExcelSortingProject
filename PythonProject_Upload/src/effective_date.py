from pathlib import Path
import pandas as pd

def remove_consecutive_duplicate_jobs(excel_path: Path, config: dict) -> None:
    """
    For each unique ID, remove consecutive rows with the same job title.
    Keeps the first row of consecutive duplicates and preserves non-consecutive duplicates.
    
    :param excel_path: Path to the Modified_ Excel file to process
    """
    # Load the Excel file
    df = pd.read_excel(excel_path)
    
    # Assume the first column is the unique ID
    id_column = config["unique_id_column"]
    job_title_column = config["job_title_column"]
    effective_date_column = config["effective_date_column"]

    # Sort by unique ID and Effective Date to ensure correct order
    df.sort_values([id_column, effective_date_column], inplace=True)

    # Function to filter consecutive duplicates within each group
    def filter_group(group: pd.DataFrame) -> pd.DataFrame:
        mask = group[job_title_column] != group[job_title_column].shift(1)
        return group[mask]

    # Apply filtering per unique ID
    df_cleaned = df.groupby(id_column, group_keys=False).apply(filter_group)

    # Overwrite the Excel file with cleaned data
    df_cleaned.to_excel(excel_path, index=False)
