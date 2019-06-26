import praw
reddit = praw.Reddit('bot1')
print(reddit.read_only);

# for submission in reddit.subreddit('learnpython').hot(limit=10):
#     print(submission.title)
# 
# subreddit = reddit.subreddit('unixporn')
# print(subreddit.display_name)
# print(subreddit.title)
# print(subreddit.description)
# for submission in subreddit.hot(limit=10):
#     print(submission.title)
#     print(submission.score)
#     print(submission.id)
#     print(submission.url)
#     redditor1 = submission.author
#     print(redditor1.name)
#     print()
# 
# redditor2 = reddit.redditor('genericSpecimen')
# print(redditor2.name)
# print(redditor2.link_karma)
# 
# submission = reddit.submission(id='c0k1tf')
# print(submission.title)
# top_level_comments = list(submission.comments)
# all_comments = submission.comments.list()
# 
# print(top_level_comments)
# print(all_comments)
# 
# import pprint
# print(submission.title)
# pprint.pprint(vars(submission))
 

print(reddit.user.me())

submission = reddit.submission(url='https://www.reddit.com/r/funny/comments/3g1jfi/buttons/')

# for top_level_comment in submission.comments:
#    print (top_level_comment.body)

# A limit of 0 simply removes all MoreComments from the forest.
#submission.comments.replace_more(limit = 0)
#for top_level_comment in submission.comments:
#    print(top_level_comment.body)

# a limit of None means that all MoreComments objects will be replaced until there are none left, as long as they satisfy the threshold.

submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    print(comment.body)

