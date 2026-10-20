# Project Documentation — Student Performance Analytics System

## 1. Project Title and Student Details
**Project:** Student Performance Analytics System  
**Student name:** Lalit Punetha  
**Course:** Python with AI   
**Date:** 18-10-2026

## 2. Objective
The objective is to build a Python program that reads student marks and attendance from a CSV file and summarizes academic performance. It helps identify individual totals and averages, grades, pass/fail status, subject strengths, and top performers.

## 3. Technologies Used
- Python
- Pandas for loading, organizing, filtering, and summarizing tabular data
- NumPy for numerical calculations
- CSV for storing student records

## 4. Dataset Description
The sample `students.csv` file contains 20 records. Columns include student ID, name, department, marks in Python, Mathematics, Statistics, AI, and English, plus attendance percentage. The data is sample data for demonstration.

## 5. Implementation
1. `main.py` reads `students.csv` with `pandas.read_csv()`.
2. The program checks that required columns exist and validates that marks and attendance are numeric and between 0 and 100.
3. `functions.py` calculates total marks and average marks for each student.
4. A function assigns grades using the grading table below.
5. A student passes only if every subject mark is at least 40.
6. NumPy calculates class-level average, highest average, and lowest average.
7. Pandas summarizes each subject and ranks students by average.
8. The program displays the analysis and saves processed records to `student_analysis_report.csv`.

### Grading rule
| Average marks | Grade |
|---:|:---|
| 90 and above | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| Below 50 | F |

### Pass/fail rule
A student passes if they score at least 40 marks in every subject. Otherwise, the result is Fail. Attendance is shown in the report but is not used to decide pass/fail.

## 6. Key Features
- Dataset loading and validation
- Total and average marks
- Grade and pass/fail calculation
- Class performance statistics
- Subject-wise average/highest/lowest marks
- Top-three student list
- Export of processed data to CSV

## 7. Output / Screenshots
After running `python main.py`, insert screenshots of:
1. The student performance table
2. Class summary
3. Subject-wise analysis and top-three performers
4. The generated `student_analysis_report.csv` file (optional)

**Screenshots:** [Insert your own screenshots here.]

## 8. Final Outcome
====================================================================
             STUDENT PERFORMANCE ANALYTICS SYSTEM
====================================================================
Dataset records: 20

STUDENT PERFORMANCE
 Student_ID           Name Department  Total_Marks  Average_Marks Grade Result  Attendance
       1001   Aarav Sharma        CSE          427           85.4     A   Pass          92
       1002     Diya Verma        CSE          375           75.0     B   Pass          85
       1003    Kabir Singh        ECE          299           59.8     D   Pass          78
       1004   Ananya Joshi        CSE          466           93.2    A+   Pass          98
       1005   Ishaan Mehta         ME          236           47.2     F   Pass          68
       1006    Meera Rawat        ECE          406           81.2     A   Pass          90
       1007   Vivaan Gupta        CSE          346           69.2     C   Pass          82
       1008      Sara Khan         IT          439           87.8     A   Pass          94
       1009     Arjun Negi         ME          208           41.6     F   Fail          61
       1010   Aditi Pandey         IT          402           80.4     A   Pass          88
       1011    Reyansh Das        ECE          305           61.0     C   Pass          74
       1012    Myra Kapoor        CSE          456           91.2    A+   Pass          96
       1013  Krishna Bisht         IT          260           52.0     D   Pass          70
       1014   Ira Malhotra        ECE          413           82.6     A   Pass          91
       1015 Atharv Chauhan         ME          292           58.4     D   Pass          76
       1016    Anvi Saxena        CSE          408           81.6     A   Pass          89
       1017     Dev Thakur         IT          192           38.4     F   Fail          55
       1018   Kiara Bansal        ECE          355           71.0     B   Pass          84
       1019    Rudra Sethi         ME          441           88.2     A   Pass          93
       1020   Saanvi Reddy         IT          329           65.8     C   Pass          80

CLASS SUMMARY
Number of students : 20
Class average      : 70.55
Highest average    : 93.2
Lowest average     : 38.4
Students passed    : 18
Students failed    : 2
Pass percentage    : 90.0%

SUBJECT-WISE ANALYSIS (ranked by average)
    Subject  Average  Highest  Lowest
    English    72.05       95      36
Mathematics    70.95       96      38
         AI    70.75       92      41
 Statistics    70.45       94      39
     Python    68.55       94      32

TOP 3 PERFORMERS
 Student_ID         Name Department  Average_Marks Grade
       1004 Ananya Joshi        CSE           93.2    A+
       1012  Myra Kapoor        CSE           91.2    A+
       1019  Rudra Sethi         ME           88.2     A

Full results saved to: student_analysis_report.csv
Chart saved to: subject_performance_chart.png

## 9. Challenges and Learning
During this project, I learned how to use Python, NumPy, and Pandas to analyze student performance data. One of the main challenges was organizing student records and performing calculations accurately. I solved this by using Pandas DataFrames to manage the dataset and NumPy to calculate averages and other statistical values.

I also learned how to create reusable functions to calculate total marks, average marks, grades, and pass/fail results. Using conditional statements helped me assign grades according to the defined grading criteria. I used loops and Pandas operations to analyze subject-wise performance and identify the top-performing students.

Another important learning experience was understanding how to read data from a CSV file, validate the input data, and save the processed results into a new CSV file.

Overall, this project improved my understanding of Python programming, data handling, functions, conditional statements, NumPy, and Pandas. It also helped me understand how data analysis can be used to summarize student performance and generate meaningful insights.

## 10. GitHub Repository
https://github.com/Terra8yte/student-performance-analytics
