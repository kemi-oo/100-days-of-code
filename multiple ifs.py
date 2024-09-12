height = int(input("what's your height in cm "))
print("hmmm.... so you're",height, "cm tall")
if height >= 120:
    age = int(input("how old are you?"))
    if age <= 12:
        bill = 5
        print("child tickets are $5")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7")
    else:
        bill = 12
        print("adult tickets are $12")
        
    wants_photo = input("Do you want to have a photo taken? Type y for yes and n for no")
    if wants_photo == "y":
        #add $3 to their bill
        bill += 3
    print(f"your final bill is {bill}")
else:
    print("sorry!! come back when you're at least 120cm tall.")