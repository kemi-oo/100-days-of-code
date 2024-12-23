#def greet():
    #user_name = input("Hello, what's your name?:\n")
    #print("Welcome!,"+user_name)
    #print("How are you doing today?")
#greet()

#functions that allows for inputs
#def greet_with_name(name):
    #print("Welcome!," + name)
    #print("How are you doing today?")
#greet_with_name("kemi")

#this function tells you how many weeks a person has left to live if we were all to live up to 90 years.
#by taking the person's age as an argument
def your_life_in_weeks(age):
    life_in_weeks = (((90-age)*365)/7)
    print(f"you have {life_in_weeks} weeks left" )
your_life_in_weeks(89)