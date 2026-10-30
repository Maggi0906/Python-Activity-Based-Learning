## Case Study 94: Disaster Relief Supply Allocation
## 1. Problem Statement
Develop a Python program to distribute disaster relief supplies among different affected areas. Compare available stock with area-wise requirements, prioritize urgent areas, allocate available supplies, and calculate remaining shortages.
## 2. Algorithm
1. Start.
2. Initialize available stock.
3. Store area-wise supply requirements.
4. Define area allocation priority.
5. Select each area according to priority.
6. Compare required quantity with available stock.
7. Allocate the minimum available quantity.
8. Calculate unmet demand and remaining stock.
9. Display allocation details.
10. Stop.
## 3. Flowchart
``` meramid

flowchart TD
    A([Start]) --> B[Initialize stock and area requirements]
    B --> C[Select highest priority area]
    C --> D[Select required supply]
    D --> E[Compare stock and demand]
    E --> F[Allocate minimum available quantity]
    F --> G[Update remaining stock]
    G --> H[Calculate unmet demand]
    H --> I{More supplies or areas?}
    I -- Yes --> D
    I -- No --> J[Display allocation summary]
    J --> K([Stop])
```
##  5. Sample Input
Available Stock:
Food: 100
Water: 150
Medicine: 60
Clothes: 80
Area A: Food 50, Water 70, Medicine 30
Area B: Food 40, Water 60, Medicine 40
Area C: Food 30, Water 50, Medicine 20
Priority: Area A, Area B, Area C
##  6. Sample Output
DISASTER RELIEF ALLOCATION
Area A
Food Required: 50
Allocated: 50
Shortage: 0
Water Required: 70
Allocated: 70
Shortage: 0
Medicine Required: 30
Allocated: 30
Shortage: 0
