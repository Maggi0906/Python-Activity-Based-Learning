## Case Study 97: Smart Campus Incident and Maintenance Prioritization
## 1. Problem Statement
Develop a Python program to manage campus maintenance reports based on severity, location, and reported frequency. Assign priority scores, rank incidents, and generate a maintenance priority summary.
## 2. Algorithm
1. Start.
2. Initialize incident records.
3. Define severity scores.
4. Read incident details.
5. Calculate priority score using severity and frequency.
6. Sort incidents in descending order.
7. Classify incidents based on severity.
8. Display the ranked maintenance report.
9. Stop.
## 3. Flowchart
``` mermaid
## 5. Sample Input
I101, Electrical Failure, High, Block A, 5
I102, Water Leakage, Medium, Block B, 3
I103, Network Failure, High, Lab, 4
I104, Broken Chair, Low, Classroom, 2
I105, Fire Alarm Failure, Critical, Block C, 5
```
## 6. Sample Output
CAMPUS INCIDENT PRIORITY REPORT

Incident ID: I105
Problem: Fire Alarm Failure
Severity: Critical
Location: Block C
Priority Score: 45
Action: Immediate Attention

Incident ID: I101
Problem: Electrical Failure
Severity: High
Location: Block A
Priority Score: 35
Action: Urgent Maintenance

Incident ID: I103
Problem: Network Failure
Severity: High
Location: Lab
Priority Score: 34
Action: Urgent Maintenance

Incident ID: I102
Problem: Water Leakage
Severity: Medium
Location: Block B
Priority Score: 23
Action: Schedule Maintenance

Incident ID: I104
Problem: Broken Chair
Severity: Low
Location: Classroom
Priority Score: 12
Action: Normal Maintenance
