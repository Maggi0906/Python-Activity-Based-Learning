stock = {
    "Python": 50,
    "Java": 40,
    "AI": 30,
    "Web": 20
}
requirements = {
    "Branch A": {
        "Python": 20,
        "Java": 15,
        "AI": 10
    },
    "Branch B": {
        "Python": 25,
        "Java": 20,
        "AI": 15
    },
    "Branch C": {
        "Python": 15,
        "Java": 10,
        "Web": 15
    }
priority = ["Branch A", "Branch B", "Branch C"]
print("LIBRARY BOOK DISTRIBUTION")
for branch in priority:
    print("\n", branch)
    for book, required in requirements[branch].items():
        allocated = min(stock[book], required)
        stock[book] -= allocated
        unmet = required - allocated
        print("\nBook:", book)
        print("Required:", required)
        print("Allocated:", allocated)
        print("Unmet Demand:", unmet)
print("\nREMAINING BOOK STOCK")
for book, quantity in stock.items():
    print(book, ":", quantity)
