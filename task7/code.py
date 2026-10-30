incidents = [
    ("I101", "Electrical Failure", "High", "Block A", 5),
    ("I102", "Water Leakage", "Medium", "Block B", 3),
    ("I103", "Network Failure", "High", "Lab", 4),
    ("I104", "Broken Chair", "Low", "Classroom", 2),
    ("I105", "Fire Alarm Failure", "Critical", "Block C", 5)
]

severity_score = {
    "Critical": 4,
    "High": 3,
    "Medium": 2,
    "Low": 1
}
ranked = []
for iid, problem, severity, location, frequency in incidents:

    score = severity_score[severity] * 10 + frequency

    ranked.append(
        (score, iid, problem, severity, location)
    )
ranked.sort(reverse=True)

print("CAMPUS INCIDENT PRIORITY REPORT")

for score, iid, problem, severity, location in ranked:

    print("\nIncident ID:", iid)
    print("Problem:", problem)
    print("Severity:", severity)
    print("Location:", location)
    print("Priority Score:", score)

    if severity == "Critical":
        print("Action: Immediate Attention")
    elif severity == "High":
        print("Action: Urgent Maintenance")
    elif severity == "Medium":
        print("Action: Schedule Maintenance")
    else:
        print("Action: Normal Maintenance")
