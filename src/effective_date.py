from pathlib import Path
import pandas as pd

def remove_consecutive_duplicate_jobs(excel_path: Path, config: dict) -> None:
    """
    For each unique ID, collapse consecutive identical job titles.
    Keeps the EARLIEST effective date for each consecutive job run.
    
    Assumes rows are already sorted by:
        last name ASC,
        unique ID ASC,
        effective date DESC
    """
    df = pd.read_excel(excel_path)

    id_column = config["unique_id_column"]
    job_title_column = config["job_title_column"]

    def collapse_job_runs(group: pd.DataFrame) -> pd.DataFrame:
        # Identify job title changes
        job_change = group[job_title_column] != group[job_title_column].shift()

        # Assign a run ID to each consecutive block
        run_id = job_change.cumsum()

        # Keep the LAST row of each run (earliest effective date)
        return group.groupby(run_id, as_index=False).tail(1)

    df_cleaned = (
        df
        .groupby(id_column, group_keys=False, sort=False)
        .apply(collapse_job_runs)
    )

    df_cleaned.to_excel(excel_path, index=False)
