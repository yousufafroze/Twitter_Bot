import tweepy
import time
import twitter_credentials.py

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
the_id = 1079598822710378496

while True:
    for thing in api.home_timeline(since_id=the_id):
        if (("intern" in thing.text) or ("internship" in thing.text)) and ("developer" in thing.text):
            the_id = thing.id
            screen_name = thing.user.screen_name
            name = thing.user.name
            try:
                api.update_status("@" + name + " heyy i really need an internship",the_id)
            except tweepy.error.TweepError:
                pass
    time.sleep(10)


    
            
