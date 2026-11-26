'''True, "Mon"
False, "Wed"
False, "Fri"
False, "Sat"
True, "Sat"
False, "wed" (lowercase)
False, "Funday"'''

# Python is case sensitive , wed!=Wed
working_tonight=False
day='Funday'



if working_tonight:
    print("Block 11:30pm to 3 am is used for coding practice and project building")
elif not working_tonight and day=='Wed':
    print("Block 6:00pm to 8:30 pm is used to reviewing and fixing")
elif not working_tonight and day=='Sat':
    print("Block 8:30am to 12:30pm used to build project")
elif not working_tonight and (day=="Thu" or day=="Fri"):
    print("Block 4:00pm to 8:00pm is used to learn new concepts")
else:
    print("Day not planned")