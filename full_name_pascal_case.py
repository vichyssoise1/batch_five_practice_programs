#User input
full_name = input("Enter your full name in incorrect casing: ")
pascal_case = full_name.title().replace(" ", "")  # Convert to PascalCase by removing spaces and capitalizing each word
print("Your name in pascal case is: ", pascal_case)