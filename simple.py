def simple_interest(p, r, t):
    return (p * r * t) / 100.0

# Example usage
if __name__ == "__main__":
    p = float(input("Principal (P): "))
    r = float(input("Rate % (R): "))
    t = float(input("Time years (T): "))
    si = simple_interest(p, r, t)
    print(f"Simple Interest = {si:.2f}")
    print(f"Amount after {t} years = {p + si:.2f}")
def compound_interest(p, r, t):
    a = p * (1 + r / 100) ** t
    ci = a - p
    return ci, a

# Example usage
p = float(input("Principal (P): "))
r = float(input("Rate % (R): "))
t = float(input("Time (years): "))

ci, a = compound_interest(p, r, t)
print(f"Compound Interest = {ci:.2f}")
print(f"Total Amount = {a:.2f}")
