'''Assignment Title: Exploring Password Validation**
**Objective:**
* To create a simple password validation system using a `while` loop with an `else` statement.
**Instructions:**
1. Write a Python program that prompts the user to enter a password.
2. The program should continue prompting the user until they enter a password 
that meets the following criteria:
   - The password must be at least 8 characters long.
   - The password must contain at least one uppercase letter.
   - The password must contain at least one lowercase letter.
   - The password must contain at least one digit (0-9).
3. If the entered password meets all the criteria, print "Password accepted!" and end the program.
4. If the entered password does not meet all the criteria after 5 attempts, 
print "Maximum attempts reached." and end the program.
5. Use a `while` loop to repeatedly prompt the user for input.
6. Utilize an `else` block with the `while` loop to handle the case when the 
password is successfully accepted or when the maximum attempts are reached.
**Example Output:**
Enter your password: abcd
Password must be at least 8 characters long.
Enter your password: Password123
Password must contain at least one lowercase letter.
Enter your password: pass
Password must be at least 8 characters long.
Enter your password: Pass123
Password accepted!
'''
attempt = 1

while attempt <= 5:
    password = input("Input password: ")
    if len(password) != 8:
        print("Password must contain eight characters.")
    elif not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
    elif not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one digit (0-9).")
    elif password == 'Pass1234':
        print("Password accepted.")
        break
    else:
        print("Invalid password.")
    
    attempt += 1
print("Total attempts:", attempt)