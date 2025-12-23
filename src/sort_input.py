from pathlib import Path
import pandas as pd

def sort_excel_by_lastname_and_id(excel_path: Path, config: dict) -> None:
    df = pd.read_excel(excel_path)

    last_name_col = config.get("last_name_column")
    id_col = config.get("unique_id_column")
    date_col = config.get("effective_date_column")

    sort_cols = []
    ascending = []

    if last_name_col in df.columns:
        sort_cols.append(last_name_col)
        ascending.append(True)

    if id_col in df.columns:
        sort_cols.append(id_col)
        ascending.append(True)

    if date_col in df.columns:
        # Ensure proper date sorting
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
        sort_cols.append(date_col)
        ascending.append(False)  # most recent first

    if sort_cols:
        df.sort_values(
            by=sort_cols,
            ascending=ascending,
            inplace=True,
            na_position="last"
        )

    df.to_excel(excel_path, index=False)
