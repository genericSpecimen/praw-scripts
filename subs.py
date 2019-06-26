import praw

reddit = praw.Reddit('bot1')
for subreddit in reddit.user.subreddits(limit=None):
    print(subreddit.display_name)

