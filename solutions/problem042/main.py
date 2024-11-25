import math
from words import WORDS

def get_val(char: str) -> int:
    return ord(char) - 64

# triangle formula = t_n = 0.5n(n+1)
# => 2t_n = n^2 + n
# => n^2 + n - 2t_n = 0

def get_det(tn: int):
    # b^2 - 4ac
    # 1 - 4(-2tn)
    # 1 + 8tn
    return 1 + 8 * tn

def calc_tn(word: str) -> int:
    char_vals = []
    for char in word:
        char_val = get_val(char)
        char_vals.append(char_val)

    return sum(char_vals)

def is_square(num: int) -> bool:
    root = math.sqrt(num)
    return root == int(root)

ans = 0

for word in WORDS:
    tn = calc_tn(word)
    det = get_det(tn)
    if is_square(det): ans += 1


print(ans)
