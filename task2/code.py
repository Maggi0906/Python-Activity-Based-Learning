events = [
    ("Cricket", "10:00", "Team A"),
    ("Football", "10:00", "Team B"),
    ("Basketball", "11:00", "Team A"),
    ("Volleyball", "12:00", "Team C"),
    ("Tennis", "11:00", "Team B")
]
scores = [
    ("Team A", 50),
    ("Team B", 40),
    ("Team C", 60),
    ("Team A", 30),
    ("Team B", 25),
    ("Team C", 20)
]
schedule = {}
conflicts = []
for event, time, team in events:
    if (team, time) in schedule:
        conflicts.append((team, time))
    else:
        schedule[(team, time)] = event
total_scores = {}
for team, points in scores:
    if team in total_scores:
        total_scores[team] += points
    else:
        total_scores[team] = points
rankings = sorted(
    total_scores.items(),
    key=lambda x: x[1],
    reverse=True
)
print("SCHEDULING CONFLICTS")
if conflicts:
    for team, time in conflicts:
        print(team, "has a conflict at", time)
else:
    print("No scheduling conflicts found")
print("\nTOTAL TEAM SCORES")
for team, points in total_scores.items():
    print(team, ":", points)
print("\nFINAL TEAM RANKINGS")
for rank, (team, points) in enumerate(rankings, start=1):
    print(rank, team, "-", points, "points")

