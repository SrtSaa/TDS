import json

# Load products from JSON file or string
with open("products.json", "r") as f:
    products = json.load(f)

# Filter products with price >= 130.06
filtered = [p for p in products if p["price"] >= 130.06]

# Sort by category (A→Z), then price (high→low), then name (A→Z)
sorted_products = sorted(
    filtered,
    key=lambda p: (p["category"], -p["price"], p["name"])
)

# Output as minified JSON string
with open("sorted_products.json", "w") as f:
    json.dump(sorted_products, f, separators=(',', ':'))

