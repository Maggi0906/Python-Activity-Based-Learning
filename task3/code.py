passengers = [
    ("P101", "Route A", "Adult"),
    ("P102", "Route B", "Student"),
    ("P103", "Route A", "Senior"),
    ("P104", "Route C", "Adult"),
    ("P105", "Route B", "Student")
]
fares = {
    "Route A": 30,
    "Route B": 40,
    "Route C": 50
}
discounts = {
    "Adult": 1.0,
    "Student": 0.5,
    "Senior": 0.7
}
expected_revenue = 0
print("PASSENGER FARE DETAILS")
for passenger in passengers:
    pid, route, category = passenger
    fare = fares[route] * discounts[category]
    expected_revenue += fare
    print(pid, route, category, "Fare:", fare)
collected_revenue = 140
difference = collected_revenue - expected_revenue
print("\nExpected Revenue:", expected_revenue)
print("Collected Revenue:", collected_revenue)
print("Difference:", difference)
if difference == 0:
    print("Revenue Successfully Reconciled")
elif difference > 0:
    print("Extra Revenue:", difference)
else:
    print("Revenue Shortage:", abs(difference))
