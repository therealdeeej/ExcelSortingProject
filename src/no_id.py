from pathlib import Path
import pandas as pd

def extract_rows_without_id(
    excel_path: Path,
    output_dir: Path,
    config: dict
) -> None:
    df = pd.read_excel(excel_path)

    id_column = config["unique_id_column"]
    first_name_col = config["first_name_column"]
    last_name_col = config["last_name_column"]

    # Normalize ID column FIRST
    raw_id_series = df[id_column]

    id_series = (
        raw_id_series
        .astype(str)
        .str.strip()
        .str.replace(r"[^\d]", "", regex=True)  # remove dashes, spaces, etc
    )

    placeholder_ids = {"", "0", "000000000"}

    missing_id_mask = (
        raw_id_series.isna() |                # real NaN
        id_series.isin(placeholder_ids)       # normalized placeholders
    )

    rows_without_id = df[missing_id_mask]
    rows_with_id = df[~missing_id_mask]

    if not rows_without_id.empty:
        sort_cols = []
        if last_name_col in rows_without_id.columns:
            sort_cols.append(last_name_col)
        if first_name_col in rows_without_id.columns:
            sort_cols.append(first_name_col)

        if sort_cols:
            rows_without_id = rows_without_id.sort_values(sort_cols)

        output_file = output_dir / "rows_missing_id.xlsx"
        rows_without_id.to_excel(output_file, index=False)

    # IMPORTANT: preserve existing order for valid rows
    rows_with_id.to_excel(excel_path, index=False)
