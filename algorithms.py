# Time complexity for Task 1 is Constant time = O(1)
#def is_even(n):
#    return n % 2 == 0

#user_number = int(input("Enter a number: "))

#result = is_even(user_number)
#print(f"{user_number} is {result}")

# Time complexity for Task 2 is Linear Time = O(n)
#def check_numbers(n):
#    for number in n:
#        if number >= 100:
#            return False
#    return True

#def display_results():
#    print(f"First list is {check_numbers(first_list)}")
#    print(f"Second list is {check_numbers(second_list)}")

#first_list = [2, 24, 68, 77, 99, 98]
#second_list = [20, 100, 96, 97, 35]

#display_results()

#Time complexity for Task 3 is Linear Time = O(n)
def check_duplicate_names(names):
    names_dictionary = {}
    for name in names:
        if name in names_dictionary:
            return True
        names_dictionary[name] = names_dictionary.get(name, 0) + 1
    return False

def display_outcome(names):
    result = check_duplicate_names(names)
    print(f"{names} is {result}!")

display_outcome(["John", "Jacob", "Jason", "Bob", "Doug"])
display_outcome(["Steven", "Terry", "Megan", "Zac", "Steven"])