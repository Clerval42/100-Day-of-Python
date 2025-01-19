target = int(input())  # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum = 0
if target > 0 and target < 1000:
    for n in range(2, target + 1, 2):
        if n % 2 == 0:
            sum += n

print(sum)
