def is_palindrome(s):
    mid = len(s) // 2

    for i in range(mid):
        if s[i] != s[-i - 1]: return False

    return True

palindromes = []

for i in range(1_000_000):
    bini = str(bin(i))[2:]

    if is_palindrome(str(i)) and is_palindrome(bini):
        palindromes.append(i)

print(sum(palindromes))
