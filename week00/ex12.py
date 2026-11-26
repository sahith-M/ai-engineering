for i in range(1,31):
    if i%3==0 and i%5==0:
        print(f"FizzBuzz")
    elif i%3==0:
        print(f"Fizz")
    elif i%5==0:
        print(f"Buzz")
    else:
        print(i)
       
        
# if i%3==0 is written first - it prints fizz for 15 , 30 because the if exits and doesn;t log for i%5==0 because it exits after first true
