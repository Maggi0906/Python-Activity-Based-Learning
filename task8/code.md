## Case Study 98: University Academic Progression Audit
## 1. Problem Statement
Develop a Python program to evaluate students' academic progression by checking semester marks, subject pass conditions, attendance percentage, and prerequisite completion. Determine whether a student is eligible for the next semester and display any outstanding requirements.
## 2. Algorithm
1. Start the program.
2. Enter student details, subject marks, attendance percentage, and prerequisite status.
3. Check whether each subject mark is at least 40.
4. Check whether attendance is at least 75%.
5. Check whether prerequisite subjects are completed.
6. Identify failed subjects and other pending requirements.
7. Display the progression eligibility report.
8. Stop the program.
## 3. Flowchart
``` mermaid

## 5. Sample Input
Enter Student Name: Yeshwitha
Enter marks in Python: 65
Enter marks in Mathematics: 35
Enter marks in Web Technology: 72
Enter Attendance Percentage: 80
Prerequisites completed? (yes/no): yes

## 6. Sample Output
===== ACADEMIC PROGRESSION REPORT =====
Student Name: Yeshwitha
Python : 65
Mathematics : 35
Web Technology : 72
Attendance: 80.0 %

Status: Not Eligible
Outstanding Requirements:
- Failed Subjects: Mathematics
