# Take input from the user
n = int(input("Enter a number: "))

# List of odd numbers less than n
odd_numbers = [x for x in range(n) if x % 2 != 0]

# Another list of odd numbers using the same logic (for example purpose)
another_odd_list = [x for x in range(1, n, 2)]

print("Odd numbers less than", n, ":", odd_numbers)
print("Another odd list:", another_odd_list)
