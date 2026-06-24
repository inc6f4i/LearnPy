data = [10, 20, 30, 40, 50, 60]
print(list(range(0, len(data), 2)))

scores = [90, 85, 77, 95, 60, 88]

a = sorted(scores, reverse=True)
for b in a[-3:]:
    print(b)
