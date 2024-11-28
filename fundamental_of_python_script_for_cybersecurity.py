# Step-by-Step Python Script for Beginners Interested in Cybersecurity

# 1. Comments and Basic Syntax
# Comments are lines in the code ignored by Python. Use them to explain what your code does.

# This is a comment explaining the purpose of the script
print("Welcome to Cybersecurity and Python Programming!")  # Print a welcome message

# 2. Data Types
# Python has different data types, such as integers, floats, strings, and booleans.

# Integer - Used for counting
num_ports = 5
print("Number of ports to check:", num_ports)

# Float - Used for precise measurements
response_time = 0.0123
print("Response time:", response_time)

# String - Used for text data
target_ip = "192.168.1.1"
print("Target IP address:", target_ip)

# Boolean - Used for true/false values
is_vulnerable = True
print("Is the system vulnerable?", is_vulnerable)

# 3. Variables and User Input
# Variables store data. You can also get input from users.

user_ip = input("Enter the IP address you want to scan: ")  # Prompt user for an IP address
print("Scanning IP address:", user_ip)

# 4. Operators
# Operators are used for calculations and comparisons.

# Arithmetic operators
a = 10
b = 3
print("Addition:", a + b)
print("Division:", a / b)
print("Modulus:", a % b)

# Comparison operators
print("Is a greater than b?", a > b)

# Logical operators
print("Is a > b and b > 0?", a > b and b > 0)

# 5. Conditional Statements
# If conditions control the flow of the program.

port = 80
if port == 80:
    print("HTTP service detected.")
else:
    print("Service not recognized.")

# Nested if statements
is_open = True
if port == 80:
    if is_open:
        print("Port 80 is open and vulnerable.")

# 6. Loops
# Loops allow you to repeat actions.

# For loop
for i in range(1, 4):
    print(f"Checking port {i}...")

# While loop
count = 1
while count <= 3:
    print(f"Attempt {count}")
    count += 1

# 7. Complex Data Types and Arrays
# Lists and dictionaries store collections of data.

# List (array)
passwords = ["admin", "12345", "letmein"]
for password in passwords:
    print("Trying password:", password)

# Dictionary
credentials = {"admin": "admin123", "guest": "guest123"}
print("Credentials:", credentials)

# 8. Functions
# Functions allow code reuse.

def scan_port(ip, port):
    print(f"Scanning {ip} on port {port}...")
    return f"Port {port} is open!"

# Call the function
result = scan_port(target_ip, 22)
print(result)

# 9. File Handling
# You can read from and write to files.

# Write to a file
with open("scan_results.txt", "w") as file:
    file.write("Port 80 is open.\n")

# Read from a file
with open("scan_results.txt", "r") as file:
    content = file.read()
    print("File Content:", content)

# 10. Modules
# Modules allow you to use external code.

import socket  # Importing the socket module for network operations

# Basic Port Scan
def basic_port_scan(ip, ports):
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open!")
            else:
                print(f"Port {port} is closed.")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# Using the function
ports_to_scan = [22, 80, 443]
basic_port_scan(target_ip, ports_to_scan)

# Summary
print("You've learned Python basics with a focus on cybersecurity!")