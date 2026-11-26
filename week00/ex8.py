try:
    hours=float(input("Enter the number of hours: "))
    print(int(hours))
except ValueError:
    print("Please enter hours in digits")

print("Program finished")


# Python cleans up the edges before reading a number 
# In case of "" the spaces returns empty number while float after reading "5  " it cuts of the space after reading a number so it returns 5