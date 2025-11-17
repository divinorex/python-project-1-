# Assignment
# Create a dicitionary and store 3 student records
# students = {
#     "student1": {"name": "John Doe", "age": 16, "grade": "A"},
#     "student2": {"name": "Mary James", "age": 17, "grade": "B"},
#     "student3": {"name": "Alex Brown", "age":15, "grade": "C"}
# }
# # print all student records
# for key, record in students.items():
#     print(f"{key}: {record}")
    

# # Create a tuple of 5 students name(print out the first value and last value)
# students = ("John", "Mary", "Alex", "Grace", "Daniel")
# # print the first and last values
# print("First student:", students[0])
# print("Last student:", students[-1])


# # Create a list of students name and print each using a for loop
# students = ["John", "Mary", "Alex", "Grace", "Daniel"]
# # Use a for loop to print each student's name
# for name in students:
#     print(name)


# # Write a python program using while loop to create a simple banking system
# balance = 0 #initial balance
# running = True

# print("Welcome to Simple Banking System!")

# while running:
#     print("\n--- MENU ---")
#     print("1. Check Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Exit")
    
#     choice = input("Enter your choice (1-4):")
#     if choice == "1":
#         print(f"Your current balance is: ${balance}")
        
#     elif choice == "2":
#         amount = float(input("Enter amount to deposit: "))
#         balance += amount
#         print(f"${amount} deposited successfully! New balance: ${balance}")
        
#     elif choice == "3":
#         amount = float(input("Enter amount to withdraw: "))
#         if amount <= balance:
#             balance -= amount
#             print(f"${amount} withdrawn successfully! New balance: ${balance}")
#         else:
#             print("Insufficient funds!")
            
#     elif choice == "4":
#         print("Thank you for banking with us. Goodbye!")
#         running = False
        
#     else:
#         print("Invalid choice! Please enter a number between 1 and 4.")



# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print("Result:" , result)

# except ZeroDivisionError:
#     print("You cannot divide by zero!")

# except ValueError:
#     print("Please enter a valid number .")

# users = {"Divine": "1234"}

# try:
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if users[username] == password:
#         print("Login successful ✅")
#     else:
#         print("Wrong password ❌")

# except:
#     print("username not found ❌")

class Car: 
        pass 
    
my_car = Car()

class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

my_car = Car("Toyota", "Red", 2023)
my_car1 = Car("Lexus", "Black", 2024)

print(my_car.brand)
print(my_car.color)
print(my_car.year)