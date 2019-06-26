import praw

reddit = praw.Reddit('bot1')

brain = open('brain', 'r')
to_sub = brain.readlines()
brain.close()

for sub in to_sub:
    subreddit = reddit.subreddit(sub.rstrip())
    print('Subscribing to: ' + subreddit.display_name)
    subreddit.subscribe()

