
x=12
count=0
while(True):

    try:
        
        n=int(input("Enter the number between 1 and 20: "))
        count=count+1
        if n==x:
            break
      
        if n>x:
            print("The input is higher")
        elif n<x:
            print("The input is smaller")
             
    except ValueError:
        print("Please enter number in digits")

print(f"You got it in {count} tries!") 