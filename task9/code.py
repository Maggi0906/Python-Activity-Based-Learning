products = {
    "Laptop": [50000, 5],
    "Mobile": [20000, 10],
    "Headphones": [2000, 15]
}

orders = {
    "Laptop": 2,
    "Mobile": 3,
    "Headphones": 4
}

dispatched = {
    "Laptop": 2,
    "Mobile": 2,
    "Headphones": 4
}

returns = {
    "Laptop": 1,
    "Mobile": 1,
    "Headphones": 0
}

discount = 10
total_revenue = 0

print("===== E-COMMERCE REPORT =====")
for product in products:
    price, stock = products[product]
    order_qty = orders[product]
    dispatch_qty = dispatched[product]
    return_qty = returns[product]
    net_qty = dispatch_qty - return_qty
    revenue = net_qty * price
    revenue = revenue - (revenue * discount / 100)
    total_revenue += revenue
    final_stock = stock - dispatch_qty + return_qty
    print("\nProduct:", product)
    print("Ordered:", order_qty)
    print("Dispatched:", dispatch_qty)
    print("Returned:", return_qty)
    print("Final Stock:", final_stock)
    print("Revenue: Rs.", revenue)

    if order_qty != dispatch_qty:
        print("Discrepancy: Order and dispatch quantity differ")
    else:
        print("Discrepancy: None")
print("\nTotal Revenue: Rs.", total_revenue)

