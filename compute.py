import data
import re

SHORTEN_IMPLEMENTED = False
LINKS_IMPLEMENTED = False
HASHTAGS_IMPLEMENTED = False
MENTIONS_IMPLEMENTED = False

def compute(tweet, shorten, links, hashtags, mentions):
	if len(tweet) == 0: return tweet

	for phrase in data.phrases.keys():
		case_insensitive_phrase = re.compile(re.escape(phrase), re.IGNORECASE)
		tweet = case_insensitive_phrase.sub(data.phrases[phrase], tweet)
	
	split_tweet = tweet.split()
	for i in range (0, len(split_tweet)):
		if split_tweet[i] in data.words: split_tweet[i] = data.words[split_tweet[i]]

	tweet = " ".join(split_tweet)

	return tweet

def shorten(tweet):
	if len(tweet) == 0: return []

	split_tweet = tweet.split()

	for phrase in data.phrases.keys():
		case_insensitive_phrase = re.compile(re.escape(phrase), re.IGNORECASE) 
		matches = re.finditer(case_insensitive_phrase, tweet)
		for m in matches:
			index = m.start(0)
			word_index = 0
			if index != []:
				word_index = len(tweet[:index].split())
			else:
				continue
			split_tweet[word_index] = data.phrases[phrase]
			for i in range (word_index + 1, len(phrase) + 1):
				split_tweet[i] = ''
	for i in range (0, len(split_tweet)):
		if split_tweet[i] in data.words: split_tweet[i] = data.words[split_tweet[i]]
	
	split_tweet_ref = tweet.split()
	shorten_result = []
	for i in range (0, len(split_tweet)):
		if split_tweet[i] != split_tweet_ref[i]:
			if split_tweet[i] == '': continue
			elif i == (len(split_tweet) - 1) or split_tweet[i+1] != '': 
				shorten_result.append({'value' : split_tweet[i], 'index' : i, 'length' : 1})
			else:
				j = 1
				print(len(split_tweet) - i)
				while j < (len(split_tweet) - i):
					if split_tweet[i+j] != '': break
					j += 1

				shorten_result.append({'value' : split_tweet[i], 'index' : i, 'length' : j})

	return shorten_result

def links(tweet):
	return False

def hashtags(tweet):
	return False

def mentions(tweet):
	return False
