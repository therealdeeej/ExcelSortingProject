from pathlib import Path
from src.output_directory import create_output_directory
from src.input_setup import tmp_setup
from src.no_id import extract_rows_without_id
from src.effective_date import remove_consecutive_duplicate_jobs
from src.config import load_config
from src.sort_input import sort_excel_by_lastname_and_id
from src.final_output import write_final_output

def main():
    # Resolve the directory where the script lives
    project_root = Path(__file__).resolve().parent
    config = load_config(project_root)

    input_dir = project_root / "input"

    output_dir = create_output_directory(project_root)
    print(f"Output directory ready at: {output_dir}")

    modified_excel = tmp_setup(input_dir)
    print(f"Working on file: {modified_excel}")

    #Step 1: sort the input file
    sort_excel_by_lastname_and_id(modified_excel, config)

    #Step 2: remove rows without ID
    extract_rows_without_id(modified_excel, output_dir, config)

    #Step 3: remove duplicate jobs
    remove_consecutive_duplicate_jobs(modified_excel, config)

    #Step 4: write final file
    output_file = write_final_output(modified_excel, output_dir, config)
    print(f"Final formatted file written to: {output_file}")

if __name__ == "__main__":
    main()
