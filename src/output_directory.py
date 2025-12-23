from pathlib import Path

def create_output_directory(project_root: Path) -> Path:
    """
    Ensure that an 'output' directory exists in the project root.
    Creates it if it does not exist.

    :param project_root: Path to the project root directory
    :return: Path to the output directory
    """
    output_dir = project_root / "output"
    output_dir.mkdir(exist_ok=True)
    return output_dir
