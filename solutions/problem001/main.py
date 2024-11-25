ans = 0

for i in range(1, 1000):
    if 0 in [i % 3, i % 5]:
        ans += i

print(ans)
