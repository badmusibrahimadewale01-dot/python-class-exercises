score = int(input("Enter your exam score (0-100): "))

# write your if/elif/else statements here
if score >= 70 and score <=100:
    print("A")
elif score >=60 and score <=69:
    print("B")
elif score >=50 and score <=59:
    print("C")
elif score >=40 and score <=49:
    print("D")
elif score >100:
    print("N/A")
else:
    print("F")

