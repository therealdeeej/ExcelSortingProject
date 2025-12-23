from pathlib import Path
import shutil

def tmp_setup(input_dir: Path) -> Path:
    """
    Copies the single Excel file from input/ into input/tmp/,
    prefixing the filename with 'Modified_'.

    The tmp directory is cleared on each run.

    :param input_dir: Path to the input directory
    :return: Path to the copied (modifiable) Excel file
    """
    tmp_dir = input_dir / "tmp"
    tmp_dir.mkdir(exist_ok=True)

    # Clean tmp directory
    for item in tmp_dir.iterdir():
        if item.is_file():
            item.unlink()

    # Find Excel files in input (excluding tmp)
    excel_files = [
        f for f in input_dir.iterdir()
        if f.is_file() and f.suffix.lower() in {".xlsx", ".xls"}
    ]

    if len(excel_files) != 1:
        raise RuntimeError(
            "Input folder must contain exactly one Excel file."
        )

    original_file = excel_files[0]
    modified_file = tmp_dir / f"Modified_{original_file.name}"

    shutil.copy2(original_file, modified_file)

    return modified_file
