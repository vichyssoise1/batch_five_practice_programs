#Add basic user input functionality to the code
full_name = input("Enter your full name with spaces at the beginning: ")
full_name = full_name.lstrip()  # Remove leading and trailing spaces
print("Your full name without leading spaces is:", full_name) 