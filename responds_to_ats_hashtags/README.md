# Bot responds to tweets when tagged and hashtag found
This bot will respond to posts that tag it and have a certain hashtag. If tweet is response to another it will respond to the original. If tweet is an original tweet it will rspond to the original tweet.

## Setup
1. Add appropriate keys
2. First make environment has python3 and tweepy installed
3. Pull code to environment
4. Edit the if/elif for the hashtag(s) you are looking for (line 54)
5. Edit whether you want to update with text or media (lines 57-61) and add appropriate text/media

## To run
1. Navigate to appropriate directory
2. You must have a valid status id in the text file or first run the code without 'last_seen_id' in line 41's parameters and comment out line 35 (to fill text file)
3. Use command: python3 main.py
4. ctrl^c to stop program
