import random
from art import LOGO,VS
from word_dictionary import INSTAGRAM_USERS_DICTIONARY
#todo - track of the highscore can be done in the future by including a text file?
def return_proffesion(user):
    return insta_users[user]["profession"]
def return_country(user):
    return insta_users[user]["country"]
def return_followers(user):
    return insta_users[user]["followers"]

def compare_followers(user_a,user_b):
    if return_followers(user_a) > return_followers(user_b):
        return True
    else:
        return False
def random_user_choice(instagram_users_dict):
    return random.choice(list(instagram_users_dict.keys()))


print(LOGO)
insta_users = INSTAGRAM_USERS_DICTIONARY

score = 0
A_user = random_user_choice(insta_users)
game = True

while(game!=False):
    B_user = random_user_choice(insta_users)
    while(A_user==B_user):
        B_user = random_user_choice(insta_users)

    print("\nCompare A: "+A_user, ',', return_proffesion(A_user), ',', return_country(A_user))
    print(VS)
    print("Against B: "+B_user, ',', return_proffesion(B_user), ',', return_country(B_user),'\n')

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    while(user_guess!='a' and user_guess!='b'):
        user_guess = input("Wrong input!Try again! Who has more followers? Type 'A' or 'B': ").lower()

    if user_guess=='a':
        if compare_followers(A_user,B_user)==True:
            score+=1
            A_user=B_user
            print("You're right! Current score: ",score)
        else:
            print("Sorry that's wrong. Final score: ",score)
            break
    if user_guess=='b':
        if compare_followers(A_user,B_user)==False:
            score+=1
            A_user=B_user
            print("You're right! Current score: ",score)
        else:
            print("Sorry that's wrong. Final score: ",score)
            break


