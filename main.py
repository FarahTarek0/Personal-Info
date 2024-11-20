
name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
is_student_input = input("Are you a student? (yes/no): ").lower()
birth_year = (2024 - age)


# all char lowercase, seprate by _ 
is_student = True if is_student_input == 'yes' else False


print("\n--- Personal Form ---")
print(f"Name: {name}")
print(f"Age: {age} years")
print(f"Height: {height} meters")
print(f"Is a student: {is_student}")
print(f"Year of Birth :{birth_year}")
