import time  # Importing library to control the speed of the program

# Getting data from the user
start = float(input("Enter a starting number: "))
end = float(input("Enter an ending number: "))
step = float(input("Enter a step number: "))
count_down_speed = float(input("Enter countdown pause time (in sec): "))

# Showing output
print("\n------- Count Down Begins! --------\n")

# Running the loop
while start > end:
    print(round(start, 2))  # Rounding for better readability
    time.sleep(count_down_speed)
    start -= step  # Decrement by step value

print("\n------- Countdown Finished! --------")
