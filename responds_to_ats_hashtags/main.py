import tweepy
import time

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

imagePath = ''

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_with_image(media, replyTo):
    api.update_with_media(media, in_reply_to_status_id=replyTo, auto_populate_reply_metadata=True)

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.

    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        
        if mention.in_reply_to_status_id is None:
            replyToStatus = mention.id
        else:
            replyToStatus = mention.in_reply_to_status_id

        print(str(mention.id) + ' - ' + mention.full_text, flush=True)

        if '#' in mention.full_text.lower():
            print('found #', flush=True)
            print('responding back...', flush=True)
            #api.update_with_media(imagePath, in_reply_to_status_id=replyToStatus,
                #auto_populate_reply_metadata=True)
            #or
            #api.update_status("text", in_reply_to_status_id=replyToStatus,
                #auto_populate_reply_metadata=True)
        elif '##' in mention.full_text.lower():
            print('found #', flush=True)
            print('responding back...', flush=True)
            #api.update_with_media(imagePath, in_reply_to_status_id=replyToStatus,
                #auto_populate_reply_metadata=True)
            #or
            #api.update_status("text", in_reply_to_status_id=replyToStatus,
                #auto_populate_reply_metadata=True)


while True:
    reply_to_tweets()
    time.sleep(15)