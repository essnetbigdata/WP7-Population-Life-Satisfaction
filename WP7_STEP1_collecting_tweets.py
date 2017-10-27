# WP7 Population Life Satisfaction Use Case
# If you need more information:
# Contact: j.maslankowski@stat.gov.pl

import tweepy 
import csv

# !!! put your keys in single quota in the four lines below
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# !!! REPLACE pl WITH YOUR COUNTRY CODE
language='pl'

# !!! REPLACE THE keyword IF YOU WANT TO COLLECT INFORMATION SPECIFIC TO THE KEYWORD
keyword=":("

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# you can use geo location if you need by, e.g., 
# api=tweepy.API(auth, geocode="51.776667, 19.454722, 300km")
api = tweepy.API(auth)


# the software will collect 5000 current tweets in selected language
hashTweet = tweepy.Cursor(api.search, q=keyword, count=5000, lang=language).items(5000)

# the name of the output file is keyword_ .csv, where space is replaced with the keyword, e.g., WP7_keyword_angry.csv
with open('WP7_keyword_%s.csv' % keyword, 'w', encoding="utf-8", errors="ignore") as f:
	f.write('id;date;tweet;language')
    for tweet in hashTweet:
        outtweets=str(tweet.id_str)+";"+str(tweet.created_at)+";"+str(tweet.text)+";"+str(tweet.lang)+"\n"
        print (tweet.text) 
        if "RT " not in outtweets:
            f.write(outtweets)