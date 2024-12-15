def generate_series(a):
    series = []
    num = 1
    while len(series) < (a if a % 2 != 0 else a - 1):
        series.append(num)
        num += 2
    return series

a = int(input("Enter an integer: "))
result = generate_series(a)
print(", ".join(map(str, result)))