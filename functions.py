"""Reusable functions for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

SUBJECTS = ["Python", "Mathematics", "Statistics", "AI", "English"]

def add_performance_columns(df):
    """Return a copy with total, average, grade, and pass/fail columns."""
    result = df.copy()
    result["Total_Marks"] = result[SUBJECTS].sum(axis=1)
    result["Average_Marks"] = np.round(result[SUBJECTS].mean(axis=1), 2)

    def grade_for(average):
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        return "F"

    result["Grade"] = result["Average_Marks"].apply(grade_for)

    # A student passes only if they score at least 40 in every subject.
    result["Result"] = result[SUBJECTS].ge(40).all(axis=1).map(
        {True: "Pass", False: "Fail"}
    )
    return result

def get_class_summary(df):
    """Return a dictionary of overall class statistics."""
    averages = df["Average_Marks"].to_numpy()
    pass_count = int((df["Result"] == "Pass").sum())
    total_students = len(df)
    return {
        "student_count": total_students,
        "class_average": round(float(np.mean(averages)), 2),
        "highest_average": round(float(np.max(averages)), 2),
        "lowest_average": round(float(np.min(averages)), 2),
        "pass_count": pass_count,
        "fail_count": total_students - pass_count,
        "pass_percentage": round(pass_count / total_students * 100, 2) if total_students else 0.0,
    }

def get_subject_summary(df):
    """Calculate average, highest, and lowest marks for every subject."""
    return pd.DataFrame({
        "Subject": SUBJECTS,
        "Average": [round(float(df[s].mean()), 2) for s in SUBJECTS],
        "Highest": [int(df[s].max()) for s in SUBJECTS],
        "Lowest": [int(df[s].min()) for s in SUBJECTS],
    }).sort_values("Average", ascending=False)

def get_top_performers(df, count=3):
    """Return the top students ranked by average marks."""
    return df.nlargest(count, "Average_Marks")[
        ["Student_ID", "Name", "Department", "Average_Marks", "Grade"]
    ]
