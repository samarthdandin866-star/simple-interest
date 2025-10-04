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
