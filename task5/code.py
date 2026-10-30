materials = {
    "Steel": 500,
    "Plastic": 300,
    "Rubber": 200
}
required = {
    "Steel": 2,
    "Plastic": 1,
    "Rubber": 1
}
demand = 150
capacities = []
for material in materials:
    capacity = materials[material] // required[material]
    capacities.append(capacity)
production = min(capacities)
print("ORDER DEMAND:", demand)
print("MAXIMUM PRODUCTION:", production)
if production >= demand:
    print("Production is feasible")
else:
    print("Production shortage:", demand - production)
defects = 8
quality_limit = 5
good_products = production - defects
print("\nPRODUCTION DETAILS")
print("Total Production:", production)
print("Defective Products:", defects)
print("Good Products:", good_products)
if defects > quality_limit:
    print("Quality Violation Detected")
else:
    print("Quality Standards Satisfied")
print("\nREMAINING MATERIALS")
for material in materials:
    used = production * required[material]
    remaining = materials[material] - used
    print(material, ":", remaining)
