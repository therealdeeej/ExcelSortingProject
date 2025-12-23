from pathlib import Path
import pandas as pd

def write_final_output(modified_excel: Path, output_dir: Path, config: dict, output_filename: str = "final_output.xlsx") -> Path:
    """
    Writes the final formatted Excel file:
    - Puts key columns first (unique ID, first name, last name, job title, effective date)
    - Preserves all other columns in their original order
    - Keeps original column names from the file
    - Optionally formats the effective date column in Excel
    
    :param modified_excel: Path to the cleaned tmp Excel file
    :param output_dir: Path to the output folder
    :param config: Dictionary containing column names
    :param output_filename: Name for the final output file
    :return: Path to the written final Excel file
    """
    df = pd.read_excel(modified_excel)
    
    # Ensure sorting by unique ID and effective date
    df.sort_values([config["unique_id_column"], config["effective_date_column"]], ascending=[True,False], inplace=True)

    # Determine column order: key columns first, then any others
    key_columns = [
        config["unique_id_column"],
        config["first_name_column"],
        config["last_name_column"],
        config["job_title_column"],
        config["effective_date_column"]
    ]

    # Preserve other columns not in key_columns
    other_columns = [col for col in df.columns if col not in key_columns]
    final_column_order = key_columns + other_columns

    df = df[final_column_order]

    # Write to Excel with formatting for the effective date column
    output_file = output_dir / output_filename
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Sheet1")
        ws = writer.sheets["Sheet1"]

        # Apply Excel date format to effective date column
        if config["effective_date_column"] in df.columns:
            date_col_idx = df.columns.get_loc(config["effective_date_column"])
            for cell in ws.iter_cols(min_col=date_col_idx + 1,
                                     max_col=date_col_idx + 1,
                                     min_row=2,
                                     max_row=ws.max_row):
                for c in cell:
                    c.number_format = "m/d/yyyy"

    return output_file
