import praw
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('askreddit')

#for comment in subreddit.stream.comments():
#    try:
#        parent_id = str(comment.parent())
#        original = reddit.comment(parent_id)
#        print('Parent: ')
#        print(original.body)
#        
#        print('Reply: ')
#        print(comment.body)
#    except praw.exceptions.PRAWException as e:
#       pass


for submission in subreddit.stream.submissions():
    try:
        print(submission.title)
    except Exception as e:
        print(str(e))

