from pathlib import Path
import pandas as pd

def extract_rows_without_id(
    excel_path: Path,
    output_dir: Path,
    config: dict
) -> None:
    """
    Extracts rows that do not have a value in the first column
    (unique ID), writes them to a new Excel file, and removes
    them from the original Excel file.

    :param excel_path: Path to the Modified_ Excel file
    :param output_dir: Path to the output directory
    """
    # Load Excel file
    df = pd.read_excel(excel_path)

    # First column is assumed to be the unique ID
    id_column = config["unique_id_column"]
    first_name_col = config["first_name_column"]
    last_name_col = config["last_name_column"]

    # Define placeholder IDs that count as "missing"
    placeholder_ids = {"0", "000-00-0000", "000000000"}

    # Convert IDs to string, strip whitespace, and check against placeholders
    id_series = df[id_column].astype(str).str.strip()

    # Rows where ID is missing or empty
    missing_id_mask = (
        id_series.isna() |                     # NaN values
        id_series.eq("") |                     # empty strings
        id_series.str.upper().isin(placeholder_ids)  # placeholder IDs
    )

    # Split the data
    rows_without_id = df[missing_id_mask]
    rows_with_id = df[~missing_id_mask]

    # Only create the output file if needed
    if not rows_without_id.empty:
        # Sort by last name, then first name
        sort_cols = []
        if last_name_col in rows_without_id.columns:
            sort_cols.append(last_name_col)
        if first_name_col in rows_without_id.columns:
            sort_cols.append(first_name_col)

        if sort_cols:
            rows_without_id = rows_without_id.sort_values(sort_cols)
            
        output_file = output_dir / "rows_missing_id.xlsx"
        rows_without_id.to_excel(output_file, index=False)

    # Overwrite the modified file with cleaned data
    rows_with_id.to_excel(excel_path, index=False)
