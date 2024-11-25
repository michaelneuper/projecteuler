coins = [1, 2, 5, 10, 20, 50, 100, 200]

def get_subsets(lst):
    if not lst: return [[]]

    first, rest = lst[0], lst[1:]

    subsets_without_first = get_subsets(rest)
    subsets_with_first = [[first] + subset for subset in subsets_without_first]

    return subsets_without_first + subsets_with_first

# 200p
subsets = get_subsets(coins)
subsets200 = [subset for subset in subsets if sum(subset) == 200]
print(subsets200)
