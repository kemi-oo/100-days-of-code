import random
import high_low_gamedata
import high_low_art

data = high_low_gamedata.data

current_score = 0
game_on = True

A = random.choice(data)
B = random.choice(data)
while game_on:
    A = B
    B = random.choice(data)

    A_name = A["name"]
    B_name = B["name"]

    A_followers = A["follower_count"]
    B_followers = B["follower_count"]

    A_description = A["description"]
    B_description = B["description"]

    A_country = A["country"]
    B_country = B["country"]
    print(high_low_art.logo)
    print(f"Compare A: {A_name}, a {A_description}, from {A_country}")
    print(high_low_art.vs)
    print(f"Against B: {B_name}, a {B_description}, from {B_country}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)

    def increase_score(current_score):
        return current_score + 1

    def user_choice():
        if choice == "A":
           answer = A_followers > B_followers
        elif choice == "B":
           answer = B_followers > A_followers

    def compare(a_followers, b_followers):
        current_score = 0
        if A_followers > B_followers and choice == "a":
            return True
        elif B_followers > A_followers and choice == "b":
            return True
        elif A_followers > B_followers and choice == "b":
            return False
        elif B_followers > A_followers and choice == "a":
            return False
    if A_followers > B_followers and choice == "a":
        current_score = increase_score(current_score)
        print(f"You're right! current score: {current_score}")
    elif B_followers > A_followers and choice == "b":
        current_score = increase_score(current_score)
        print(f"You're right! current score: {current_score}")
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        break
    def play_game():
      user_choice()
      compare(A_followers, B_followers)

    play_game()



