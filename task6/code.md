## Case Study 96: Multi-Criteria Library Resource Distribution
## 1. Problem Statement
Develop a Python program to distribute library books among different branches based on their requirements and available stock. Allocate books according to branch priority and calculate unmet demand and remaining stock.
## 2. Algorithm
1. Start.
2. Initialize book stock.
3. Store branch-wise book requirements.
4. Define branch allocation priority.
5. Select a branch.
6. Compare available stock with required quantity.
7. Allocate available books.
8. Calculate unmet demand.
9. Update remaining stock.
10. Display the allocation report.
11. Stop.
## 3.flowchart 
``` mermaid
    A([Start]) --> B[Enter Book Stock and Demand]
    B --> C[Check Branch Requirements]
    C --> D[Allocate Books by Priority]
    D --> E[Calculate Unmet Demand]
    E --> F[Display Allocation Report]
    F --> G([End])
```
## 5. Sample Input
Available Books:
Python: 50
Java: 40
AI: 30
Web: 20

Branch A: Python 20, Java 15, AI 10
Branch B: Python 25, Java 20, AI 15
Branch C: Python 15, Java 10, Web 15

Priority:
Branch A
Branch B
Branch C
## 6. Sample Output
LIBRARY BOOK DISTRIBUTION

Branch A

Book: Python
Required: 20
Allocated: 20
Unmet Demand: 0

Book: Java
Required: 15
Allocated: 15
Unmet Demand: 0

Book: AI
Required: 10
Allocated: 10
Unmet Demand: 0

Branch B

Book: Python
Required: 25
Allocated: 25
Unmet Demand: 0

Book: Java
Required: 20
Allocated: 20
Unmet Demand: 0

Book: AI
Required: 15
Allocated: 15
Unmet Demand: 0

Branch C

Book: Python
Required: 15
Allocated: 5
Unmet Demand: 10

Book: Java
Required: 10
Allocated: 5
Unmet Demand: 5

Book: Web
Required: 15
Allocated: 15
Unmet Demand: 0

REMAINING BOOK STOCK
Python : 0
Java : 0
AI : 5
Web : 5
