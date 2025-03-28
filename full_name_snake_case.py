#User input
full_name = input("Enter your full name in incorrect casing: ")
snake_case = full_name.lower().replace(" ", "_")  # Convert to snake case
print("Your name in snake case is:", snake_case)