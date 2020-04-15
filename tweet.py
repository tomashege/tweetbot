import sys
import tweepy 
import datetime
import hide as info # key information
d = info.data
# getting all the Auth things right

auth = tweepy.OAuthHandler(d['API_key'], d['API_secret_key']) 
auth.set_access_token(d['Access_token'] , d['Access_token_secret'])
api = tweepy.API(auth)

text = ""
if len(sys.argv)==1:
    print("You can add the tweet to to the end of the call (python3 tweet.py my first tweet)")
    text = input("What do you want to tweet? ")
else:
    text = ' '.join(sys.argv[1:])
    # remove the first list entry since its the name of the python script
    
# now that we have the message we will be ready to go and send the tweet 
api.update_status(text)
print("your message has been sent out")