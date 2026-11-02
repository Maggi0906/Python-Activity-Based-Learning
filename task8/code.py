name = input("Enter Student Name: ")
subjects = ["Python", "Mathematics", "Web Technology"]
marks = []
for subject in subjects:
    mark = int(input("Enter marks in " + subject + ": "))
    marks.append((subject, mark))
attendance = float(input("Enter Attendance Percentage: "))
prerequisite = input("Prerequisites completed? (yes/no): ").lower()
failed_subjects = []
for subject, mark in marks:
    if mark < 40:
        failed_subjects.append(subject)
pending = []

if failed_subjects:
    pending.append("Failed Subjects: " + ", ".join(failed_subjects))

if attendance < 75:
    pending.append("Attendance below 75%")

if prerequisite != "yes":
    pending.append("Prerequisites not completed")

print("\n===== ACADEMIC PROGRESSION REPORT =====")
print("Student Name:", name)

for subject, mark in marks:
    print(subject, ":", mark)

print("Attendance:", attendance, "%")
if len(pending) == 0:
    print("Status: Eligible for Next Semester")
else:
    print("Status: Not Eligible")
    print("Outstanding Requirements:")
    for item in pending:
        print("-", item)

