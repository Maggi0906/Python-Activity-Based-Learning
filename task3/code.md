## Case Study 93: Smart Public Transport Fare Reconciliation
## 1. Problem Statement
Develop a Python program to calculate passenger fares for different routes and passenger categories. Apply discounts for students and senior citizens, calculate expected revenue, compare it with collected revenue, and identify discrepancies.
## 2. Algorithm
1. Start.
2. Store passenger details, route fares, and discount rates.
3. Read each passenger record.
4. Calculate fare according to route and passenger category.
5. Calculate total expected revenue.
6. Enter collected revenue.
7. Compare expected and collected revenue.
8. Display revenue difference and discrepancy.
9. Stop.
## 3. Flowchart
```meramid
flowchart TD
    A([Start]) --> B[Initialize passenger records and fares]
    B --> C[Read passenger details]
    C --> D[Calculate discounted fare]
    D --> E[Add fare to expected revenue]
    E --> F{More passengers?}
    F -- Yes --> C
    F -- No --> G[Enter collected revenue]
    G --> H[Calculate revenue difference]
    H --> I{Difference equals zero?}
    I -- Yes --> J[Revenue reconciled]
    I -- No --> K[Display surplus or shortage]
    J --> L([Stop])
    K --> L
```
## 5. Sample Input
P101, Route A, Adult
P102, Route B, Student
P103, Route A, Senior
P104, Route C, Adult
P105, Route B, Student
Collected Revenue: 140
## 6. Sample Output
PASSENGER FARE DETAILS
P101 Route A Adult Fare: 30.0
P102 Route B Student Fare: 20.0
P103 Route A Senior Fare: 21.0
P104 Route C Adult Fare: 50.0
P105 Route B Student Fare: 20.0
Expected Revenue: 141.0
Collected Revenue: 140
Difference: -1.0
Revenue Shortage: 1.0
