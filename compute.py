import data
import re

SHORTEN_IMPLEMENTED = False
LINKS_IMPLEMENTED = False
HASHTAGS_IMPLEMENTED = False
MENTIONS_IMPLEMENTED = False

def contains(s):
	for i in range (0, len(data.words)):
		if (s.lower() == data.words[i]): return i
	return -1

def compute(tweet, shorten, links, hashtags, mentions):
	return tweet

def shorten(tweet):
	return False
#	if (len(tweet) == 0): return tweet
#	tweet = " ".join(tweet.strip().split())
#	for i in range (0, len(data.phrases)):
#		case_insensitive_phrase = re.compile(re.escape(data.phrases[i]), re.IGNORECASE)
#		tweet = case_insensitive_phrase.sub(data.short_phrases[i], tweet)
#	
#	split_tweet = tweet.split()
#	for i in range (0, len(split_tweet)):
#		j = contains(split_tweet[i])
#		if (j != -1): split_tweet[i] = data.short_words[j]
#
#	tweet = " ".join(split_tweet)
#
#	return tweet

def links(tweet):
	return False

def hashtags(tweet):
	return False

def mentions(tweet):
	return False
