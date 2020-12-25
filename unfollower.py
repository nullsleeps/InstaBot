#this one unfollows a certain amount of people you want to unfollow
from instapy import instapy


session = instapy(username = "username", password = "password")
# In the username section put you're instagram username there and in the password section put your instagram password
session.login()

session.unfollow_users(amount = 10, allFollowing = True, sleep_delay = 20)
#change the amount (10 by defualt) to the amount of people you want to unfollow