# Student Performance Analytics System

A beginner-friendly Python data-analysis project that processes student marks and attendance using **Python, NumPy, and Pandas**.

## Features
- Reads student records from `students.csv` into a Pandas DataFrame.
- Calculates each student's total and average marks.
- Assigns a grade using the rule below.
- Identifies pass/fail status.
- Reports class average, highest and lowest averages, and pass percentage.
- Compares subjects by average, highest, and lowest marks.
- Lists the top three students.
- Exports the processed results to `student_analysis_report.csv`.

## Grade and pass rules
Grades are based on average marks:
- A+: 90 and above
- A: 80–89.99
- B: 70–79.99
- C: 60–69.99
- D: 50–59.99
- F: below 50

A student passes only when they score **at least 40 in every subject**. Attendance is reported but does not affect the pass/fail result.

## Requirements
- Python 3.9 or newer recommended
- NumPy
- Pandas

Install dependencies:
```bash
python -m pip install -r requirements.txt
```

## Run the project
Keep `main.py`, `functions.py`, and `students.csv` in the same folder, then run:
```bash
python main.py
```

## Project files
- `main.py` — loads data, validates it, and displays analysis
- `functions.py` — reusable analysis functions
- `students.csv` — sample dataset containing 20 records
- `Project_Documentation.md` — report template and implementation notes
- `requirements.txt` — required Python packages

## Dataset note
The included names and marks are sample data for demonstration, not official student records. Replace or adapt the sample dataset if your instructor expects your own data, and make sure your final documentation describes the data you actually used.
