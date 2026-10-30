Case Study 92: Multi-Event Sports Scheduling and Scoring
1. Problem Statement
Develop a Python program to manage multiple sports events using lists and tuples. The program should store event schedules and team scores, identify scheduling conflicts, calculate the total points scored by each team, and generate final team rankings based on their total points.
2. Algorithm
1. Start the program.
2. Create a list of sports events using tuples containing event name, time, and team names.
3. Check the schedules and identify teams participating in multiple events at the same time.
4. Store team scores in a list of tuples.
5. Calculate the total points scored by each team.
6. Sort the teams in descending order of total points.
7. Display scheduling conflicts.
8. Display total scores and final rankings.
9. Stop the program.
3. Flowchart
mermaid
flowchart TD
    A([Start]) --> B[Enter Event Schedules]
    B --> C[Check Scheduling Conflicts]
    C --> D[Enter Team Scores]
    D --> E[Calculate Total Points]
    E --> F[Sort Teams by Points]
    F --> G[Display Conflicts and Rankings]
    G --> H([End])
5. Sample Input
Event Schedules:
Cricket      10:00    Team A
Football     10:00    Team B
Basketball   11:00    Team A
Volleyball   12:00    Team C
Tennis       11:00    Team B
Team Scores:
Team A - 50
Team B - 40
Team C - 60
Team A - 30
Team B - 25
Team C - 20
6. Sample Output
SCHEDULING CONFLICTS
No scheduling conflicts found
TOTAL TEAM SCORES
Team A : 80
Team B : 65
Team C : 80
FINAL TEAM RANKINGS
1 Team A - 80 points
2 Team C - 80 points
3 Team B - 65 points
