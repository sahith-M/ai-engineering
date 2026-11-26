# n=5 -> 15
#n=1 -> 1
#n=0 -> 0 
#for loop range always exclude the stop number
try:
    n=int(input("Enter the number: "))
    x=0
    for i in range(1,n+1):
        x=i+x
    print(x)
except ValueError:
    print("Please enter number in digits")







