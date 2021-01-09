from instapy import InstaPy

session = InstaPy(username="king_instabot", password="ilikepython")
session.login()

session.set_relationship_bounds(True, max_followers=200)
session.set_do_follow(True, percentage=100)
session.set_do_like(True, percentage=100)
session.like_by_tags(["memes", "dankmemes", "funnymemes"], amount=10)
session.do_comment_liked_photo(True, percentage=100)
session.set_comments(comments=["funny", "i like memes", "very funny", "this is great lol"])

session.end()