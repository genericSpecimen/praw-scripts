import praw

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('news')
hot_python = subreddit.hot(limit = 3)
for submission in hot_python:
    if not submission.stickied:
        print ('Title: {}, ups: {}, downs: {}, Have we visited: {}'.format(submission.title,
                        submission.ups,
                        submission.downs,
                        submission.visited))
        submission.comments.replace_more(limit=0)
        comments = submission.comments.list()
        for comment in comments:
             print (20 * '-')
             print ('Parent ID:', comment.parent())
             print ('Comment ID:', comment.id)
             print (comment.body)

