students = []
attendance = []
marks = []
events = []
while True:
    print("\n1.Add Student")
    print("2.Mark Attendance")
    print("3.Add Marks")
    print("4.Register Event")
    print("5.Display Records")
    print("6.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        students.append((roll, name))
    elif choice == "2":
        roll = input("Enter Roll No: ")
        status = input("Enter Attendance: ")
        attendance.append((roll, status))
    elif choice == "3":
        roll = input("Enter Roll No: ")
        mark = int(input("Enter Marks: "))
        marks.append((roll, mark))
    elif choice == "4":
        roll = input("Enter Roll No: ")
        event = input("Enter Event: ")
        events.append((roll, event))
    elif choice == "5":
        print("Students:", students)
        print("Attendance:", attendance)
        print("Marks:", marks)
        print("Events:", events)
    elif choice == "6":
        print("Total Students:", len(students))
        print("Total Events:", len(events))
        print("Thank You!")
        break
    else:
        print("Invalid Choice")
