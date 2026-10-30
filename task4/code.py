stock = {
    "Food": 100,
    "Water": 150,
    "Medicine": 60,
    "Clothes": 80
}
requirements = {
    "Area A": {"Food": 50, "Water": 70, "Medicine": 30},
    "Area B": {"Food": 40, "Water": 60, "Medicine": 40},
    "Area C": {"Food": 30, "Water": 50, "Medicine": 20}
}
priority = ["Area A", "Area B", "Area C"]
print("DISASTER RELIEF ALLOCATION")
for area in priority:
    print("\n", area)
    for item, required in requirements[area].items():
        allocated = min(stock[item], required)
        stock[item] -= allocated
        shortage = required - allocated
        print(item, "Required:", required)
        print("Allocated:", allocated)
        print("Shortage:", shortage)
print("\nREMAINING STOCK")
for item, quantity in stock.items():
    print(item, ":", quantity)
