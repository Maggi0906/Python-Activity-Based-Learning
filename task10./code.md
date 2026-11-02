## Case Study 100: Comprehensive Smart Campus Management Simulation
## 1. Problem Statement
Develop a Python program to manage student details, attendance, marks, events, and campus resources using lists, tuples, loops, and conditional statements.
## 2. Algorithm
1. Start the program.
2. Display the main menu.
3. Select an operation.
4. Add student, attendance, marks, event, or resource details.
5. Display campus records.
6. Repeat until the user selects Exit.
7. Display the summary and stop.
## 3. Flowchart
``` mermaid
flowchart TD
    A([Start]) --> B[Display Menu]
    B --> C[Select Operation]
    C --> D[Update Campus Records]
    D --> E{Exit?}
    E -- No --> B
    E -- Yes --> F[Display Summary]
    F --> G([End])
```
## 5. Sample Input
1
101
Yeshwitha
2
101
Present
3
101
85
4
101
AI Workshop
6

## 6. Sample Output
Total Students: 1
Total Events: 1
Thank You!
