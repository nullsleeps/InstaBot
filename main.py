from instapy import instapy


session = instapy(username = "username", password = "password")
# In the username section put you're instagram username there and in the password section put your instagram password
session.login()
session.set_relationship_bounds(enabled = True, max_followers = 300)
#change the max followers to the amount you want
session.set_do_follow(True, percentage = 100)
session.like_by_tags(["Unix", "Linux", "Python", "BSD", "MacOS", "Kernel"], amount = 4)
#change the tags to what you want to like and comment on
session.set_dont_like(["Windows", "Microsoft"])
#change these tags to what you don't want to like and comment on