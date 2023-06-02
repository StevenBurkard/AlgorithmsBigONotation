# Time complexity for Task 1 is Constant time- O(1)
def is_even(n):
    return n % 2 == 0

user_number = int(input("Enter a number: "))

result = is_even(user_number)
print(f"{user_number} is {result}")

