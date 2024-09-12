maths_score = int(input("Enter your Maths Score "))
english_score = int(input("Enter your English Score "))
if maths_score >= 90:
    if english_score >= 90:
        print("you're good at everything")
else:
    print("you're good at maths")
if english_score == 90:
    print("you're good at english")