target=30/7
print(target)
hours_studied=2

# If prints the first statement it encounters as true - it does not check for remaining conditions
if target-0.5 <= hours_studied <= target+0.5:
    print( hours_studied, "On Target" , target)
elif hours_studied<target:
    print(f"Your study target is {target:.2f} but you clocked {hours_studied}")
else:
    print("Over the target" ,hours_studied) 

# f""  to concatenate any value ---  string and {int} ---- float:.2f to round the decimal