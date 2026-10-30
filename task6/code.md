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
