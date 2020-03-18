import tweepy
import time
import csv
import pandas as pd

#twitter consumer tokens being defined here
auth = tweepy.OAuthHandler("IUK4LzRRBjNZSPse0Yrh0ASzs", "R7wgP61StMDNKtSN71hWTj7ROjIa15m8643bfm9Cy8XsUG6BSR")
#twitter access tokens being defined here
auth.set_access_token("1226323598144458754-gAWJFxK7fzoioaPomxaUS7PemHhDIl", "MtMZOPHtFyTmAu14zwRRrgJNUZx8gDZUuItwXIz8VFMHv")
#twitter api call being set here
api = tweepy.API(auth, wait_on_rate_limit=True)

with open('visualize.csv', 'w') as file:
    fieldnames=['time', 'user']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for tweet in tweepy.Cursor(api.search,q="#metoo", lang='en').items():
        writer.writerow({'time': tweet.created_at,'user':tweet.user.screen_name})
        #print (tweet.created_at, tweet.user.location)
    
