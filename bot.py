import praw
import time
import os
import pdb
import re
import random


def main():
    reddit = praw.Reddit('bot')
    subred = reddit.subreddit('College_Prestige')
    risingSubs = ['all', 'funny','memes','dankmemes','wallstreetbets']
    index = 0
    while True:
        print("--------------------------------------")
        # Get top 5 rising posts in the risingSubs list
        for submission in reddit.subreddit(risingSubs[index]).rising(limit=5):
            print(submission.title)
            #print(submission.permalink)
            #print(submission.url)
            urlLink = None
            selfText = None
            #Determines if it is a selftext or a url post
            if len(submission.selftext) != 0:
                selfText = submission.selftext
            else:
                urlLink = submission.url
            #Posts it with title, time of post, subreddit it was from
            Title = submission.title+' from r/'+risingSubs[index]+' at '+time.ctime(time.time())
            subred.submit(Title, selftext=selfText, url=urlLink , spoiler=submission.spoiler,
            nsfw=submission.over_18)
            #Mark down the post was made
            with open('posts_made.txt','a') as f:
                try:
                    f.write(submission.permalink+'\n')
                except:
                    f.write('\n')
            time.sleep(random.randint(1,5))
            #Create permalink of original post as a comment

            time.sleep(random.randint(1,5))
        #move on to the next subreddit
        index = (index+1)%(len(risingSubs))
        #wait up to 10 minutes
        sleeptime = random.randint(60,600)
        print('Sleeping for '+sleeptime+' seconds')
        time.sleep(sleeptime)

if __name__ == "__main__":
    main()