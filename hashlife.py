import tweepy
import csv
import pandas as pd
#tokens initialized
consumer_key = 'IUK4LzRRBjNZSPse0Yrh0ASzs'
consumer_secret = 'R7wgP61StMDNKtSN71hWTj7ROjIa15m8643bfm9Cy8XsUG6BSR'
access_token = '1226323598144458754-gAWJFxK7fzoioaPomxaUS7PemHhDIl'
access_token_secret = 'MtMZOPHtFyTmAu14zwRRrgJNUZx8gDZUuItwXIz8VFMHv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#Open/Create a file to append data
csvFile = open('tweets.csv', 'w')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#security",count=100,
                           lang="en",
                           since="2019-10-03").items():
    #print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.user.screen_name, tweet.text.encode('utf-8')])

csv = pd.read_csv('tweets.csv',names=["Username","Tweet"])
count = csv['Username'].value_counts()[:]
csv.head(10)

top2 = count.head(10)
top2

import matplotlib.pyplot as plt

colors =  ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]
top2.plot.pie(y=top2.index,
           shadow=False,
           colors=colors, 
           radius = 1000,
           #explode=(0, 0),   # exploding 'Friday'
           startangle=90,
           autopct='%1.1f%%',
           textprops={'fontsize': 10})

plt.axis('equal')
plt.tight_layout()
plt.show()
