#!chirpapp/bin/python
from flask import Flask, jsonify, url_for, make_response, request
import compute

application = Flask(__name__)

@application.route('/')
def get_settings():
	return jsonify({'uri' : url_for('get_new_tweet', _external = True),
					'uri_verbose' : url_for('get_new_tweet_verbose', _external = True),
					'shorten' : compute.SHORTEN_IMPLEMENTED,
					'links' : compute.LINKS_IMPLEMENTED,
					'hashtags' : compute.HASHTAGS_IMPLEMENTED,
					'mentions' : compute.MENTIONS_IMPLEMENTED })

# Aborts or returns tweet with extra whitespace removed
def handle_request(request):
	if not request.json or not 'tweet' in request.json:
		abort(400)
	return " ".join(request.json['tweet'].strip().split())

@application.route('/chirpapp/api/v1.0/tweet', methods = ['POST'])
def get_new_tweet():
	tweet = handle_request(request)

	shorten = (not 'shorten' in request.json) or (request.json['shorten'])
	links = (not 'links' in request.json) or (request.json['links'])
	hashtags = (not 'hashtags' in request.json) or (request.json['hashtags'])
	mentions = (not 'mentions' in request.json) or (request.json['mentions'])

	return jsonify({'tweet' : compute.compute(tweet, shorten, links, hashtags, mentions)}), 201

@application.route('/chirpapp/api/v1.0/tweet_verbose', methods = ['POST'])
def get_new_tweet_verbose():
	tweet = handle_request(request)

	return jsonify({'shorten' : compute.shorten(tweet),
					'links' : compute.links(tweet),
					'hashtags' : compute.hashtags(tweet),
					'mentions' : compute.mentions(tweet) })

@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__ == '__main__':
	application.run(host='0.0.0.0', debug=False)
