try:
    n=int(input("Enter the number: "))
    for i in range(1,11):
        print(f" {n} X {i} = {n*i}")
        
except ValueError:
    print("Please enter number in digits")
