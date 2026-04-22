# ============================================
# Task 1 — Tuples
# ============================================

# Create tuple
cities = ("Hyderabad", "Bangalore", "Chennai", "Mumbai", "Delhi")

# Unpack tuple
c1, c2, c3, c4, c5 = cities

# Print variables
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)

# Try modifying tuple
try:
    cities[0] = "Pune"
except TypeError as e:
    print("Error: Tuples are immutable and cannot be modified.")


print("\n============================================\n")


# ============================================
# Task 2 — Sets
# ============================================

python_passed = {"Ajay", "Ravi", "Sneha", "Kiran"}
sql_passed = {"Sneha", "Kiran", "Amit", "Neha"}

# Union
print("Union:", python_passed | sql_passed)

# Intersection
print("Intersection:", python_passed & sql_passed)

# Difference (Python-only)
print("Python-only:", python_passed - sql_passed)


print("\n============================================\n")


# ============================================
# Task 3 — Lists and ASCII
# ============================================

ascii_values = [65, 66, 67, 68, 69]

for val in ascii_values:
    print(f"{val} -> {chr(val)}")

# ASCII of 'Z'
print("ASCII of 'Z':", ord('Z'))


print("\n============================================\n")


# ============================================
# Task 4 — Subprocess
# ============================================

import subprocess

result = subprocess.run(["whoami"], capture_output=True, text=True)

print("Current user:", result.stdout.strip())
