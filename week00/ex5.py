score=41

if score<0 or score>100:
    print("invalid score")
elif score<=40:
    print("Failed.... Please spend 3 more days on this phase")
elif score<=80:
    print("Passed...Move to next phase")
else:
    print("Strong pass...Move on and keep it up")