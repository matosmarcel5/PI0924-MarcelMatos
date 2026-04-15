nums = []

for i in range(3):
    nums.append(int(input(f"Num{i+1}: ")))

print("Crescente:", sorted(nums))
print("Decrescente:", sorted(nums, reverse=True))