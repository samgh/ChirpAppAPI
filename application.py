#!chirpapp/bin/python
from flask import Flask, jsonify, url_for, make_response
import shorten

application = Flask(__name__)

@application.route('/chirpapp/api/v1.0/<string:tweet>', methods = ['GET'])
def get_new_tweet(tweet):
	return jsonify( {'tweet' : shorten.shorten(tweet)})

@application.route('/')
def get_uri():
	return jsonify({'uri' : url_for('get_new_tweet', tweet="URL_ENCODED_TWEET", _external = True)})

@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__ == '__main__':
	application.run(host='0.0.0.0', debug=False)
