
"""Student Performance Analytics System.

Run with: python main.py
Dataset: students.csv (stored in the same folder)
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from functions import (
    SUBJECTS,
    add_performance_columns,
    get_class_summary,
    get_subject_summary,
    get_top_performers,
)


def main():
    # Locate the dataset beside this Python file.
    data_file = Path(__file__).with_name("students.csv")

    try:
        students = pd.read_csv(data_file)
    except FileNotFoundError:
        print("Error: students.csv was not found beside main.py.")
        return
    except pd.errors.EmptyDataError:
        print("Error: students.csv is empty.")
        return
    except pd.errors.ParserError:
        print("Error: Could not read the CSV file correctly.")
        return

    # Check that all required columns are present.
    required_columns = [
        "Student_ID",
        "Name",
        "Department",
        *SUBJECTS,
        "Attendance",
    ]

    missing = [
        column for column in required_columns
        if column not in students.columns
    ]

    if missing:
        print("Error: Missing required columns:", ", ".join(missing))
        return

    if students.empty:
        print("Error: The dataset has no student records.")
        return

    # Validate marks and attendance.
    numeric_columns = SUBJECTS + ["Attendance"]

    for column in numeric_columns:
        students[column] = pd.to_numeric(
            students[column], errors="coerce"
        )

    if students[numeric_columns].isnull().any().any():
        print("Error: Marks and attendance must contain valid numbers.")
        return

    if not students[SUBJECTS].apply(
        lambda column: column.between(0, 100).all()
    ).all():
        print("Error: Subject marks must be between 0 and 100.")
        return

    if not students["Attendance"].between(0, 100).all():
        print("Error: Attendance must be between 0 and 100.")
        return

    # Calculate student performance and class statistics.
    results = add_performance_columns(students)
    summary = get_class_summary(results)
    subject_summary = get_subject_summary(results)
    toppers = get_top_performers(results)

    # Display the main report.
    print("\n" + "=" * 68)
    print("             STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 68)

    print(f"Dataset records: {len(results)}")

    print("\nSTUDENT PERFORMANCE")
    print(
        results[
            [
                "Student_ID",
                "Name",
                "Department",
                "Total_Marks",
                "Average_Marks",
                "Grade",
                "Result",
                "Attendance",
            ]
        ].to_string(index=False)
    )

    print("\nCLASS SUMMARY")
    print(f"Number of students : {summary['student_count']}")
    print(f"Class average      : {summary['class_average']}")
    print(f"Highest average    : {summary['highest_average']}")
    print(f"Lowest average     : {summary['lowest_average']}")
    print(f"Students passed    : {summary['pass_count']}")
    print(f"Students failed    : {summary['fail_count']}")
    print(f"Pass percentage    : {summary['pass_percentage']}%")

    print("\nSUBJECT-WISE ANALYSIS (ranked by average)")
    print(subject_summary.to_string(index=False))

    print("\nTOP 3 PERFORMERS")
    print(toppers.to_string(index=False))

    # Save the processed student report.
    output_file = Path(__file__).with_name(
        "student_analysis_report.csv"
    )
    results.to_csv(output_file, index=False)
    print(f"\nFull results saved to: {output_file.name}")

    # Create a bar chart comparing subject averages.
    plt.figure(figsize=(9, 5))

    bars = plt.bar(
        subject_summary["Subject"],
        subject_summary["Average"],
    )

    plt.title("Average Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.3)

    # Display the average value above each bar.
    for bar, average in zip(
        bars, subject_summary["Average"]
    ):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            average + 1,
            f"{average:.2f}",
            ha="center",
            va="bottom",
        )

    plt.tight_layout()

    # Save the chart beside main.py.
    chart_file = Path(__file__).with_name(
        "subject_performance_chart.png"
    )
    plt.savefig(chart_file, dpi=150, bbox_inches="tight")
    print(f"Chart saved to: {chart_file.name}")

    # Display the chart window.
    plt.show()


if __name__ == "__main__":
    main()
