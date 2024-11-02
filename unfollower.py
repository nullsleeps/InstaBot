from instapy import InstaPy

# Enter Your Instagram Login Details.
session = InstaPy(username="your_username", password="your_password")
session.login()

# Unfollow users
session.unfollow_users(amount=10, allFollowing=True, sleep_delay=20)

session.end()
