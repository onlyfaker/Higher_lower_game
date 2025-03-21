#todo - generate a random key from a list of instagram users
#todo - compare random 2 ones and see which one has more followers,
#todo - take the B answer and make it an A anser if you are correct, and generate a random one for another B answer
#todo - continue until you are wrong and show final score
import random

from art import LOGO,VS
from word_dictionary import INSTAGRAM_USERS_DICTIONARY

print(LOGO)
insta_users = INSTAGRAM_USERS_DICTIONARY
random_choice = random.choice(list(insta_users.keys()))
print(random_choice)

print(insta_users[random_choice]["followers"])
# for item in insta_users:
