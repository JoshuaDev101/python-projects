grade = float(input("Grade: "))

if grade > 100 or grade < 0:
    print("Invalid grade")
elif grade >= 97.50:
    print("1.00")
elif grade >= 94.50:
    print("1.25")
elif grade >= 91.50:
    print("1.50")
elif grade >= 86.50:
    print("1.75")
elif grade >= 81.50:
    print("2.00")
elif grade >= 76.00:
    print("2.25")
elif grade >= 70.50:
    print("2.50")
elif grade >= 65.00:
    print("2.75")
elif grade >= 59.50:
    print("3.00")
else :
    print("5.00")
