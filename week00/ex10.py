# n=20 -> 11
# n=7 -> 4

try:
    n=int(input("Enter the number: "))
    x=0
    for i in range(0,n+1):
        if i%2==0:
            x=x+1
    print(f"Number of even numbers between 0 and {n} is {x}")
        
    
except ValueError:
    print("Please enter number in digits")