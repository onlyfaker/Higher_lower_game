import random
from art import LOGO,VS
from word_dictionary import INSTAGRAM_USERS_DICTIONARY

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


A_user = random_user_choice(insta_users)
B_user = random_user_choice(insta_users)

print(A_user,',',return_proffesion(A_user),',',return_country(A_user),return_followers(A_user))
print(VS)
print(B_user,',',return_proffesion(B_user),',',return_country(B_user),return_followers(B_user))

#todo - user choice who has more follower and check if got it right
#todo - count the score of each correct guess
#todo - see if when one user is compared, can you get the same user agai or not
#todo - take the B answer and make it an A anser if you are correct, and generate a random one for another B answer
#todo - continue until you are wrong and show final score

