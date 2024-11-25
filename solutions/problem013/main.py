file = open("numbers.txt")

nums = [line for line in file]
eleven_digits = [int(num[:11]) for num in nums]

print(nums)
print(eleven_digits)

print(str(sum(eleven_digits))[:10])
