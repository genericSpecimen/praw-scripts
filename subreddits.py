import praw

reddit = praw.Reddit('bot2')
with open('file1', 'w') as file1, open('file2', 'w') as file2:
    for subreddit in reddit.user.subreddits(limit=None):
        if subreddit.over18:
            file1.write(subreddit.display_name + '\n')
        else:
            file2.write(subreddit.display_name + '\n')
file1.close()
file2.close()

