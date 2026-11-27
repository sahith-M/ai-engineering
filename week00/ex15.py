'''
break leaves the loop completely.
continue skips the rest of this round and jumps back to the top of the loop.'''

n = int(input("Enter the number of days: "))
i = 1
total = 0

while i <= n:
    try:
        x = float(input(f"Enter the number of hours studied on DAY{i}: "))
    except ValueError:
        print("Please enter number in digits")
        continue
    i += 1
    total += x

if n > 0:
    target = 30 / 7
    average = total / n

    print(f" Total hours: {total:.2f}")
    print(f" Average per day : {average:.2f}")

    if target - 0.5 <= average <= target + 0.5:
        print("On the target")
    elif average < target:
        print("Under the target")
    else:
        print("Over the daily target")
else:
    print("Enter atleast 1 day")
