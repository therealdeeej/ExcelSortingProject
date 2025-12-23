# Data Processing Tool

This tool processes and cleans up payroll data.

---

## First-Time Setup (Only Needed Once)

Before using the tool for the first time, Python and required libraries must be installed.

1. Go to https://www.python.org/downloads/ and download the Python install manager
2. Follow the setup steps ensuring you check the box that says Add Python to PATH
3. You will be asked three questions, type "y" and hit enter. The 4th is an online help question, type "n" and hit enter
4. After Python is installed, open the command prompt
5. Run the following commands:\
   ```python -m pip install --upgrade pip```\
   ```python -m pip install pandas```\
   ```python -m pip install openpyxl```


---

## How to Use the Tool

1. Place **one Excel file** into the **`input`** folder  
   - Only one file should be in this folder at a time

2. Open config.json with any text editor
   - modify the column names in quotations to match exactly as they are in the excel file
   - be careful not to change any formatting (removing commas, quotations, etc)

3. Right-click inside the project folder (not on a file)
4. Select **"Open in Terminal"** or **"Open Command Prompt here"**

5. Run the following command: python main.py

6. The tool will create an **`output`** folder (if it does not already exist) and create two files:
   - rows_missing_id (list of employees without an ID)
   - final output file with duplicate job titles removed

---

## Notes

- This tool currently supports **one Excel file at a time**
- Do not rename folders
- Close the Excel file before running the tool

---

## Troubleshooting

- Don't. It's hopeless.
- Ensure Python is available by running: python --version

---
