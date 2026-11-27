try:
    n=int(input("Enter the number: "))

    while(n>0):
        print(n)
        n=n-1
        
    print("Go!")  
except ValueError:
    print("Please enter number in digits")
