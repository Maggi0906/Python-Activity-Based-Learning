## Case Study 95: Integrated Manufacturing Production Planner
## 1. Problem Statement
Develop a Python program to analyze raw material availability, production requirements, order demand, and defective products. Calculate maximum production capacity, identify material shortages, and determine whether quality standards are satisfied.
## 2. Algorithm
1. Start.
2. Initialize available raw materials.
3. Define material requirements per product.
4. Enter order demand.
5. Calculate maximum production capacity for each material.
6. Identify the minimum production capacity.
7. Compare production capacity with order demand.
8. Calculate defective and good products.
9. Check quality standards.
10. Display remaining materials.
11. Stop.
## 3.flowchart TD
    A([Start]) --> B[Enter Materials and Production Data]
    B --> C[Check Demand and Defects]
    C --> D{Production Feasible?}
    D --> E[Identify Shortages and Quality Issues]
    E --> F[Display Production Report]
    F --> G([End])
