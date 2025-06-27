dict = {"Prarthana":98,"Neeraj":97,"Manashree":84,"Ritesh":78}

name = input("Enter the student's name: ")

if name in dict:
    print(f"{name}'s marks: {dict[name]}")
else:
    print("Student not found.")