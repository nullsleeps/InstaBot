from instapy import InstaPy

# Enter Your Instagram Login Details
session = InstaPy(username="your_username", password="your_password")
session.login()

# Set the max follower limit
session.set_relationship_bounds(enabled=True, max_followers=300)

# Enable liking and following
session.set_do_follow(True, percentage=100)
session.set_do_like(True, percentage=100)

# Like posts by specific tags
session.like_by_tags(["Cats", "Cars", "Memes", "Funny", "Drift", "Rich"], amount=4)

# Exclude certain tags
session.set_dont_like(["News", "Girls"])


session.end()
