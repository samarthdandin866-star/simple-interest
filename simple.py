# Program to calculate Simple Interest and Compound Interest

def simple_interest(p, r, t):
    """Calculate Simple Interest"""
    return (p * r * t) / 100

def compound_interest(p, r, t):
    """Calculate Compound Interest"""
    amount = p * (1 + r / 100) ** t
    return amount - p

# --- Main Program ---
p = float(input("Enter Principal Amount (P): "))
r = float(input("Enter Rate of Interest (R): "))
t = float(input("Enter Time (in years) (T): "))

# Calculate interests
si = simple_interest(p, r, t)
ci = compound_interest(p, r, t)

# Display results
print("\n----- Results -----")
print(f"Simple Interest = {si:.2f}")
print(f"Compound Interest = {ci:.2f}")
print(f"Total Amount (SI) = {p + si:.2f}")
print(f"Total Amount (CI) = {p + ci:.2f}")
