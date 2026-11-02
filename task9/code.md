## Case Study 99: Integrated E-Commerce Order Processing and Reconciliation
## 1. Problem Statement
Develop a Python program to process e-commerce product orders, apply discounts, manage dispatched products and returns, update stock quantities, calculate total revenue, identify order discrepancies, and generate a final inventory report.
## 2. Algorithm
1. Start the program.
2. Store product names, prices, and initial stock.
3. Enter ordered and dispatched quantities.
4. Calculate the 10% discount on dispatched products.
5. Enter returned quantities.
6. Calculate net revenue after returns.
7. Update final stock quantities.
8. Identify differences between ordered and dispatched quantities.
9. Display revenue, discrepancies, and final inventory.
10. Stop the program.
## 3. Flowchart
``` mermaid
flowchart TD
    A([Start]) --> B[Enter Product and Order Details]
    B --> C[Calculate Discount and Revenue]
    C --> D[Process Returns]
    D --> E[Update Stock]
    E --> F[Check Order Discrepancies]
    F --> G[Display Final Report]
    G --> H([End])
```
## 5. Sample Input
Laptop:
Price = 50000
Initial Stock = 5
Ordered = 2
Dispatched = 2
Returned = 1

Mobile:
Price = 20000
Initial Stock = 10
Ordered = 3
Dispatched = 2
Returned = 1

Headphones:
Price = 2000
Initial Stock = 15
Ordered = 4
Dispatched = 4
Returned = 0

Discount = 10%


## 6. Sample Output
===== E-COMMERCE REPORT =====
Product: Laptop
Ordered: 2
Dispatched: 2
Returned: 1
Final Stock: 4
Revenue: Rs. 45000.0
Discrepancy: None

Product: Mobile
Ordered: 3
Dispatched: 2
Returned: 1
Final Stock: 9
Revenue: Rs. 18000.0
Discrepancy: Order and dispatch quantity differ

Product: Headphones
Ordered: 4
Dispatched: 4
Returned: 0
Final Stock: 11
Revenue: Rs. 7200.0
Discrepancy: None

Total Revenue: Rs. 70200.0
