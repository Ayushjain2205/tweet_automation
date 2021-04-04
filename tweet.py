import tweepy
import time
import random

# Set Twitter API KEYS
consumer_key = '< Your Key >'
consumer_secret = '< Your Key >'
access_token = '< Your Key >'
access_token_secret = '< Your Key >'


# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

good_morning_messages = [
    'A new day has come with so many new opportunities for you. Grab them all and make the best out of your day. Here’s me wishing you a good morning!',
    'No matter how difficult yesterday was, just know that today is your day. Stay positive at every moment of your life. Good morning.',
    'Rise and shine, and get ready for another exciting sunny day! Good morning!',
    'May this day go as beautifully as you want and give you many surprises! Good morning to you.',
    'My heart is full of love for you. You are the sunshine of my life. Because of you, my life is so colorful. Good morning, my love!',
    'Wishing you a successful day ahead my dear. You have just received yet another chance to rise and shine like a diamond. Good Morning!',
    'I hope this day brightens up your life and makes you energized for work. Good morning!']

good_evening_messages = [
    'Follow your heart; Heart takes you to the destination, Where your goodness dwells, Have a happy evening!',
    'The evening is like a small pause that gives you rest enjoy this evening with your family and makes it the best Good Evening.',
    'The evening comes with the cool breeze that allows you to forget about the day and look ahead tomorrow. Please rest and have a fun evening. ― Good Evening',
    'If you can look at the sunset and smile, then you still have hope. ― Good Evening',
    'Relax yourself evening has come. Enjoy yourself night is going to go, Prepare yourself morning is yet to come. Have a good evening!',
    'You will always be kept in my mind. Just relax and enjoy your evening. Good evening my friend!',
    'The evening starts with sunset and fresh cool air. It’s time to breathe in peace. Now pack your bag with full ease, see outside, and feel freshness everywhere. Good Evening wishes.']

# Send good morning tweet
api.update_status(random.choice(good_morning_messages))

# Wait for 8 hours to send good evening tweet
time.sleep(28800)

api.update_status(random.choice(good_evening_messages))
