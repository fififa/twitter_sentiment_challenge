#Credits to Calistatee whose csv writer and URL extractor function I used for this twitter sentiment analysis challenge

import tweepy
import csv
from urlextract import URLExtract
from textblob import TextBlob

# log in via codes provided by Twitter
consumer_key= 'l03BF4ld29RJQX8l7yy61DmSh'
consumer_secret= 'cPlYKd0Ob9xSXnpNN7HjysCS6d5JJvg3T3UnZvOJg2fytwYyxb'

access_token='623982915-5D0yMN9GcaiAJA24HFpLjGB7fi5SRQyqP4KhezI3'
access_token_secret='xsl1nqy9EGbFqo0Lv6rN60ToLS5Jp59Tbu4j5qzPVRaZO'

# this is for authentication by using OAuthHandler and set_access_token method
# from tweepy with a bunch of codes hidden to us
FF_auth = tweepy.OAuthHandler(l03BF4ld29RJQX8l7yy61DmSh, cPlYKd0Ob9xSXnpNN7HjysCS6d5JJvg3T3UnZvOJg2fytwYyxb)
FF_auth.set_access_token(623982915-5D0yMN9GcaiAJA24HFpLjGB7fi5SRQyqP4KhezI3, xsl1nqy9EGbFqo0Lv6rN60ToLS5Jp59Tbu4j5qzPVRaZO)

# main variables where we'll do all the twitter magic
api = tweepy.API(FF_auth)

# now, we want to search for tweets

# create a public var to store a list of tweets
# .search method will retrieve a bunch of tweets with the designated word (MeToo)

#Step 3 - Retrieve Tweets
public_tweets = api.search('alueducation')

# to export to .csv
# 'with open' helps close your file automatically
with open('twitter_alu_sentimentanalysis.csv', 'w', newline = '') as output:

    # create var
    fileOut = csv.writer(output)
    data = [['Tweets', 'Polarity', 'Subjectivity', 'Feeling_label', 'URL']] #5 columns

#Write a function to define 'Feeling' as positive or negative based on the polarity scores.
def feeling(x):
    if x <0.2:
        return 'negative'
    if x > 0.6:
        return 'positive'
    else:
        return 'neutral'

 #Populate the csv with rows containing those 4 pieces of lingo
    fileOut.writerows(data)  

    for tweet in public_tweets:
        analysis = TextBlob(tweet.text) #sentiment analyzer model.
        polarity = analysis.sentiment.polarity        
        Feeling_label = feeling(polarity)
        subjectivity = analysis.sentiment.subjectivity

        # We want to extract any URLs contained in the tweets too. 
        #The default value for url
        # if url = None, perform operations on tweet.text to cut off existing url
        url = None

        # to start a separate column for URL
        # split texts into chunks
        words = tweet.text.split()

        # to extract link...
        link = URLExtract()

        # find links within a tweet
        urls = link.find_urls(tweet.text)

        # identify link - http / https (http is common denominator for both)
        for word in words:
            #print (word)
            if 'http' in word:
                url = word
        
        #Unresolved: deciding on the labels for positive or negative sentiments

                
        fileOut.writerow([tweet.text, polarity, subjectivity, Feeling_label, url])

        # print to terminal
        print (tweet.text)
        print ('Polarity: ', polarity)
        print ('Polarity_feeling: ', Feeling_label)
        print ('Subjectivity:', subjectivity)
        
 # check your CSV file for clean results!


