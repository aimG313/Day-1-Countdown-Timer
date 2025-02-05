import time #importing library to control the speed of the program

#getting data from the users
start = int(input("Enter a starting number:"))
end = int(input("Enter a ending number:"))
step = int(input("Enter a step number:"))
count_down_speed = int(input("Enter countdown pause time(in sec):"))

# Showing output
print("\n-------Count Down Begines!--------\n")


#running the loop with user's inut 
for i in range(start,end,-step):
  print(i)
  time.sleep(count_down_speed)
print("\n-------Countdown finished!--------")