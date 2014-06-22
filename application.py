#!chirpapp/bin/python
from flask import Flask, jsonify, url_for, make_response, request
import shorten

application = Flask(__name__)

@application.route('/chirpapp/api/v1.0/tweet', methods = ['POST'])
def get_new_tweet():
	#if not request.json or not 'tweet' in request.json:
	#	abort(400)
	#tweet = request.json['tweet']
	return jsonify({'tweet' : 'test'}), 201#shorten.shorten(tweet)}), 200

@application.route('/')
def get_uri():
	return jsonify({'uri' : url_for('get_new_tweet', _external = True)})

@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__ == '__main__':
	application.run(host='0.0.0.0', debug=False)
