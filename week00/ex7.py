day_1=float(input("Enter the  hours studied on Day 1: "))
day_2=float(input("Enter the  hours studied on Day 2: "))
day_3=float(input("Enter the  hours studied on Day 3: "))



target=30/7

total=day_1+day_2+day_3
average= total/3

print(f" Total hours: {total:.2f}")
print(f" Average per day : {average:.2f}")

if  target-0.5<= average<= target+0.5:
    print("On the target")
elif average< target:
    print("Under the target")
else:
    print("Over the daily target")
