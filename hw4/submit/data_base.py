# Importing Libraries and Setting Paths
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

HERE = Path(__file__).parent
DATA_FOLDER = HERE / "data"

# Data Importation and Cleaning
roster = pd.read_csv(DATA_FOLDER / 'roster.csv')
roster['NetID'] = roster['NetID'].str.lower()
roster['Email Address'] = roster['Email Address'].str.lower()
roster = roster.set_index('NetID')

hw_exam_grades = pd.read_csv(DATA_FOLDER / 'hw_exam_grades.csv')
hw_exam_grades['SID'] = hw_exam_grades['SID'].str.lower()
hw_exam_grades = hw_exam_grades[hw_exam_grades.columns[~hw_exam_grades.columns.str.contains('Submission')]]
hw_exam_grades = hw_exam_grades.set_index('SID')

quiz_files = DATA_FOLDER.glob('quiz_*_grades.csv')
quiz_grades = pd.DataFrame()
for file_path in quiz_files:
    quiz_name = file_path.stem.split('_grades')[0]
    df = pd.read_csv(file_path)
    df.rename(columns={'Grade': quiz_name}, inplace=True)
    df.set_index('Email', inplace=True)

    if quiz_grades.empty:
        quiz_grades = df
    else:
        quiz_grades = quiz_grades.join(df, how='outer', lsuffix='_left', rsuffix='_right')

# Merge the two dataframes on their indices (which are now both 'NetID')
final_data = pd.merge(roster, hw_exam_grades, left_index=True, right_index=True)

# Data Merging: Final data and quiz grades
overlap_cols = final_data.columns.intersection(quiz_grades.columns)
quiz_grades_reduced = quiz_grades.drop(columns=overlap_cols)
final_data = pd.merge(final_data, quiz_grades_reduced, left_on='Email Address', right_index=True)
final_data = final_data.fillna(0)

# Data Processing and Score Calculation
n_exams = 3
for n in range(1, n_exams + 1):
    score_pattern = f'Exam {n}'
    max_points_pattern = f'Exam {n} - Max Points'
    exam_score_col = final_data.filter(regex=score_pattern).columns[0]
    exam_max_col = final_data.filter(regex=max_points_pattern).columns[0]
    final_data[f'Exam {n} Proportion'] = final_data[exam_score_col] / final_data[exam_max_col]

# Calculating Exam Scores
homework_scores = final_data.filter(regex='Homework \d+$')
homework_max_points = final_data.filter(regex='Homework \d+ - Max Points')
sum_of_hw_scores = homework_scores.sum(axis=1)
sum_of_hw_max = homework_max_points.sum(axis=1)
final_data["Total Homework"] = sum_of_hw_scores / sum_of_hw_max

average_hw_scores = final_data[homework_scores.columns].div(final_data[homework_max_points.columns].values).mean(axis=1)
final_data["Average Homework"] = average_hw_scores

# Final Homework Score Calculation
final_data["Homework Score"] = np.maximum(final_data["Total Homework"], final_data["Average Homework"])

# Calculating Total and Average Quiz Scores
quiz_scores = final_data.filter(regex='quiz_')
quiz_max_points = pd.Series({"quiz_1": 11, "quiz_2": 15, "quiz_3": 17, "quiz_4": 14, "quiz_5": 12})
sum_of_quiz_scores = quiz_scores.sum(axis=1)
sum_of_quiz_max = quiz_max_points.sum()
final_data["Total Quizzes"] = sum_of_quiz_scores / sum_of_quiz_max

average_quiz_scores = (quiz_scores / quiz_max_points).mean(axis=1)
final_data["Average Quizzes"] = average_quiz_scores

# Final Quiz Score Calculation
final_data["Quiz Score"] = np.maximum(final_data["Total Quizzes"], final_data["Average Quizzes"])

# Calculating the Final Score
weightings = pd.Series({"Exam 1": 0.05, "Exam 2": 0.1, "Exam 3": 0.15, "Quiz Score": 0.30, "Homework Score": 0.4})
final_data["Final Score"] = (final_data["Exam 1 Proportion"] * weightings["Exam 1"] +
                             final_data["Exam 2 Proportion"] * weightings["Exam 2"] +
                             final_data["Exam 3 Proportion"] * weightings["Exam 3"] +
                             final_data["Quiz Score"] * weightings["Quiz Score"] +
                             final_data["Homework Score"] * weightings["Homework Score"])

# Rounding Up the Final Score
final_data["Ceiling Score"] = np.ceil(final_data["Final Score"] * 100)

# Defining Grade Mapping
grades = {90: "A", 80: "B", 70: "C", 60: "D", 0: "F"}

# Applying Grade Mapping to Data
def grade_mapping(value):
    for threshold, grade in grades.items():
        if value >= threshold:
            return grade
    return "F"

final_data["Final Grade"] = final_data["Ceiling Score"].apply(grade_mapping)

# Processing Data by Sections
for section, table in final_data.groupby("Section"):
    sorted_table = table.sort_values(by=["Last Name", "First Name"])
    file_name = f"section_{section}_grades.csv"
    file_path = DATA_FOLDER / file_name
    sorted_table.to_csv(file_path)
    print(f"Section: {section}, Students: {len(sorted_table)}, File Saved: {file_path}")

# Visualizing Grade Distribution
grade_counts = final_data['Final Grade'].value_counts().sort_index()
grade_counts.plot(kind='bar', title='Grade Distribution')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.show()

# Histogram and Kernel Density Estimate
plt.figure(figsize=(10, 6))
final_data["Final Score"].plot.hist(bins=20, alpha=0.5, label="Histogram")
final_data["Final Score"].plot.density(linewidth=4, label="Kernel Density Estimate")
plt.title('Distribution of Final Scores')
plt.xlabel('Final Score')
plt.ylabel('Density')
plt.legend()
plt.show()

# Plotting Normal Distribution
final_mean = final_data["Final Score"].mean()
final_std = final_data["Final Score"].std()
x = np.linspace(final_mean - 5*final_std, final_mean + 5*final_std, 100)
normal_distribution = scipy.stats.norm.pdf(x, final_mean, final_std)
plt.figure(figsize=(10, 6))
final_data["Final Score"].plot.hist(bins=20, alpha=0.5, label="Histogram")
final_data["Final Score"].plot.density(linewidth=4, label="Kernel Density Estimate")
plt.plot(x, normal_distribution, label='Normal Distribution', color='green', linewidth=2)
plt.title('Distribution of Final Scores with Normal Distribution Overlay')
plt.xlabel('Final Score')
plt.ylabel('Density')
plt.legend()
plt.show()
