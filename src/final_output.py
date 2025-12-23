import pandas as pd
from pathlib import Path

def write_final_output(
    modified_excel: Path,
    output_dir: Path,
    config: dict,
    output_filename: str = "final_output.xlsx"
) -> Path:
    """
    Writes the final formatted Excel file:
    - Reorders columns (does NOT reorder rows)
    - Puts key columns first
    - Preserves all unused columns
    - Formats the effective date column
    """
    df = pd.read_excel(modified_excel)

    key_columns = [
        config["unique_id_column"],
        config["first_name_column"],
        config["last_name_column"],
        config["job_title_column"],
        config["effective_date_column"]
    ]

    other_columns = [col for col in df.columns if col not in key_columns]
    final_column_order = key_columns + other_columns
    df = df[final_column_order]

    output_file = output_dir / output_filename
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Sheet1")
        ws = writer.sheets["Sheet1"]

        if config["effective_date_column"] in df.columns:
            date_col_idx = df.columns.get_loc(config["effective_date_column"]) + 1
            for row in ws.iter_rows(min_row=2,
                                    min_col=date_col_idx,
                                    max_col=date_col_idx):
                for cell in row:
                    cell.number_format = "m/d/yyyy"

    return output_file
