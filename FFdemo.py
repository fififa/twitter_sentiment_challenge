import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'l03BF4ld29RJQX8l7yy61DmSh'
consumer_secret= 'cPlYKd0Ob9xSXnpNN7HjysCS6d5JJvg3T3UnZvOJg2fytwYyxb'

access_token='623982915-5D0yMN9GcaiAJA24HFpLjGB7fi5SRQyqP4KhezI3'
access_token_secret='xsl1nqy9EGbFqo0Lv6rN60ToLS5Jp59Tbu4j5qzPVRaZO'

FF_auth = tweepy.OAuthHandler(l03BF4ld29RJQX8l7yy61DmSh, cPlYKd0Ob9xSXnpNN7HjysCS6d5JJvg3T3UnZvOJg2fytwYyxb)
FF_auth.set_access_token(623982915-5D0yMN9GcaiAJA24HFpLjGB7fi5SRQyqP4KhezI3, xsl1nqy9EGbFqo0Lv6rN60ToLS5Jp59Tbu4j5qzPVRaZO)

api = tweepy.API(FF_auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('alueducation')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.csv)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
