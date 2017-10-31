import tweepy
from textblob import TextBlob
from textblob.blob import TextBlob
import csv
import datetime


#
# @author Beloved Egbedion
#

""" 
This code scrapes twitter data through tweepy from a date range 
using since and until attributes in format : "%Y-%m-%d %H:%M" 
over the first 999999 items
It analyses the tweets and stores the output in a csv file in rows
path: /TwitterSentiments/Sentiments.py

"""


Consumer_Key='XXXXXX'
Consumer_Secret='XXXXXXXXXXX'
Access_Token='XXXXXXXXXXXXXXXX'
Access_Token_Secret='XXXXXXXXXXXXXXXXXXXX'

oauth= tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Token_Secret)

service = tweepy.API(oauth)
# select_tweets_since = datetime.datetime.strptime("2017-10-28 15:30:00", '%Y-%m-%d %H:%M:%S')
# select_tweets_until = datetime.datetime.strptime("2017-10-28 16:00:00", '%Y-%m-%d %H:%M:%S')
#tweets = service.search('Manchester')
#print(tweets)


# Open/create a file to append data to
csvFile = open('../result_2017-10-28_1530.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(service.search,
                           q = "Manchester",
                           since = datetime.datetime.strptime("2017-10-21 00:00", "%Y-%m-%d %H:%M"),
                           until = datetime.datetime.strptime("2017-10-31 00:00", "%Y-%m-%d %H:%M"),
                           lang = "en").items(999999):

    analysis = TextBlob(tweet.text)
    print(analysis.polarity)
    #Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print([tweet.created_at, tweet.text])
csvFile.close()



