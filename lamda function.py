def ahsik(a, b):
    sum = a + b
    print(sum)


ahsik(20, 10)

print("\n")
# lamda is a small and anonymous finction .
# It did the previous job in just two line.

sum = lambda a, b: a + b
print(sum(20, 10))

x = lambda q, w, e, r: (q + w) / (e - r)
print(x(10, 20, 10, 5))
