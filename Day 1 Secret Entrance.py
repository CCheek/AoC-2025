# the idea is that there exists a rotation lock with numbers from 0 to 99, we must find how many times the number hits zero (like it stops on 0)
password = 0 # initial password, to be incremented every time we hit zero.
current_number = 50 # starting point of the rotation lock

def increment_password(input_data): # Main function for processing each line of input
    global current_number
    direction = input_data[0] # First character indicates direction
    input_data = input_data[1:] # Remaining characters indicate the amount to move
    if direction == 'R':
        current_number += int(input_data)
    elif direction == 'L':
        current_number -= int(input_data)
    current_number = current_number % 100 # Wrap around using modulo 100
    if current_number == 0: 
        return True # Return True if we hit zero, otherwise return false
    return False

puzzle_input = open("puzzle input day 1.txt").read() # Access the puzzle input
for line in puzzle_input.splitlines(): # Split each line of the input and process each one
    if increment_password(line): # Check if we hit zero
        password += 1

print("The final password is:", password)