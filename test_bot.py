import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit('test')

template = """Greetings and Salutations, fellow tester.
It seems your comment contains the word 'test'.

Here's your random test image [test]({}).

^(Beep boop, I am a bot.)
This action was performed automatically."""


for comment in subreddit.comments(limit=10):
    if 'test' in comment.body:
        print('test found!')
        comment.reply(template.format('https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/SMPTE_Color_Bars.svg/1024px-SMPTE_Color_Bars.svg.png'))


