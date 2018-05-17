#Credits to Siraj raval for the challenge and 
# Calistatee whose csv writer I used for this twitter sentiment analysis challenge

import tweepy
import csv
from urlextract import URLExtract
from textblob import TextBlob

# log in via codes provided by Twitter
consumer_key= 'consumer_key'
consumer_secret= 'consumer_secret'

access_token='access_token'
access_token_secret='access_token_secret'

#  this is for authentication by using OAuthHandler and set_access_token method
# from tweepy with a bunch of codes hidden to us
FF_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
FF_auth.set_access_token(access_token, access_token_secret)

# main variables where we'll do all the twitter magic
api = tweepy.API(FF_auth)

#Step 1 - Write a function to define 'Feeling' as positive or negative based on the polarity scores.
def feeling(x):
    if x <0:
        return 'negative'
    if x > 0.5:
        return 'positive'
    else:
        return 'neutral'


#Step 2 - parameters of search
since_date = "2018-05-01"
until_date = "2018-05-17"

# Step 3 - now, we want to search for tweets


#Step 3 - Retrieve Tweets
alu_tweets = api.search('alueducation', count = 100,  since = since_date, until=until_date)

# create a public var to store a list of tweets
# .search method will retrieve a bunch of tweets with the designated word (alueducation)

# to export to .csv
# 'with open' helps close your file automatically
with open('alu_tweets.csv', 'w', newline = '') as output:

    # create var
    fileOut = csv.writer(output)
    data = [['Tweets', 'Polarity', 'Subjectivity', 'Feeling_label', 'URL']] #5 columns

 #Populate the csv with rows containing those 5 pieces of lingo
    fileOut.writerows(data)  

    for tweet in alu_tweets:
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
        

                
        fileOut.writerow([tweet.text, polarity, subjectivity, Feeling_label, url])

        # print to terminal
        print (tweet.text)
        print ('Polarity: ', polarity)
        print ('Polarity_feeling: ', Feeling_label)
        print ('Subjectivity:', subjectivity)
        
 # check your CSV file for clean results!

#BONUS
#Get the mean of the polarities
    print('Mean Polarity:', np.mean(polarity))
#It's the Mean Polarity: 0.4666666666666666 - positive but closer to neutral.
 
#Print a bar chart of the negative vs neutral vs the positive labels
df = pd.read_csv('alu_tweets.csv')
sns.set_style("whitegrid")
sns.boxplot(x="Feeling_label", y="Polarity",
                data=df)


