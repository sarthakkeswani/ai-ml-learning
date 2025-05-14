#Matrix Math and Grade Analyzer

import numpy as np

grades = np.array([
    [85, 78, 90],
    [70, 88, 75],
    [92, 85, 89]
])

print("Grade Matrix:\n", grades)

print('Shape: ', grades.shape)
print("Rows (students): ", grades.shape[0])
print('Columns (subjects): ', grades.shape[1])

print('Student A Maths: ', grades[0, 0])

student_avg = np.mean(grades, axis=1) #Row-Wise
subject_avg = np.mean(grades, axis=0) #Column-Wise

print("Max per student:", np.max(grades, axis=1))


'''MINI PROJECT'''

import numpy as np

grades=np.array([
    [85, 78, 90],
    [70, 88, 75],
    [92, 85, 89],
    [60, 72, 68],
    [89, 94, 90]
])

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
subjects = ['Math', 'Science', 'English']

avg_students = np.mean(grades,axis=1)
print('\n Average Score Per Student:')
for name, avg in zip(students,avg_students):
    print(f"{name}: {avg:.2f}")

avg_subjects = np.mean(grades, axis=0)
print('\n Average Score per Subject:')
for subject, avg in zip(subjects,avg_subjects):
    print(f"{subject}:{avg:.2f}")

topper_index= np.argmax(avg_students)
print(f"\n Topper: {students[topper_index]}with average {avg_students[topper_index]:.2f}")

weights = np.array([0.3, 0.3, 0.4])
final_scores = np.dot(grades, weights)
print("\nWeighted Final Scores:")
for name, score in zip(students, final_scores):
    print(f"{name}: {score:.2f}")