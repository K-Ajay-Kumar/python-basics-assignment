# ============================================
# Task 1 — Create and Serialise a Nested JSON Object
# ============================================

import json

student = {
    "name": "Ajay",
    "age": 24,
    "passed": True,
    "marks": [88, 76, 95],
    "address": {
        "city": "Hyderabad",
        "pincode": 500001
    }
}

# Convert to formatted JSON string
student_json = json.dumps(student, indent=4)
print("Serialized JSON:\n", student_json)


print("\n============================================\n")


# ============================================
# Task 2 — Parse JSON and Access Values
# ============================================

parsed_data = json.loads(student_json)

print("Name:", parsed_data["name"])
print("Second Mark:", parsed_data["marks"][1])
print("City:", parsed_data["address"]["city"])


print("\n============================================\n")


# ============================================
# Task 3 — Identify and Fix Invalid JSON
# ============================================

# Errors in original JSON:
# 1. Keys must be in double quotes → name is not quoted
# 2. Trailing comma is not allowed after last key-value pair

bad_json = '{ name: "Raj", "score": 88, "active": true, }'

# Fixed JSON
fixed_json = '{ "name": "Raj", "score": 88, "active": true }'

parsed_fixed = json.loads(fixed_json)
print("Fixed JSON Parsed:", parsed_fixed)


print("\n============================================\n")


# ============================================
# Task 4 — Build a JSON Array of Objects
# ============================================

products = [
    {"product_name": "Laptop", "price": 70000, "in_stock": True},
    {"product_name": "Mouse", "price": 500, "in_stock": True},
    {"product_name": "Keyboard", "price": 1500, "in_stock": False}
]

products_json = json.dumps(products, indent=2)
print("Products JSON:\n", products_json)
