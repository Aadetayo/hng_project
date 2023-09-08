# endpoint.py
import os
import json
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

endpoint = Flask(__name__)

@endpoint.route('/api', methods=['GET'])
def input_required():
    
    #get slack name from the url  
    getSlackName = request.args.get('slack_name', 'example_name')

    #get slack track from the url 
    getTrack = request.args.get('track', 'backend')
    
    #get current day and time in UTC format  
    getDayTime = datetime.utcnow().strftime('%A')

    #modify the time, subtract two minutes following the format 
    getTime = (datetime.utcnow() - timedelta(minutes=2)).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    #
    repoFileLink = 'https://github.com/username/repo/blob/main/file_name.ext'
    repoLink = 'https://github.com/username/repo'
    
    response_data = {
        "slack_name": getSlackName,
        "current_day": getDayTime,
        "utc_time": getTime,
        "track": getTrack,
        "github_file_url": repoFileLink,
        "github_repo_url": repoLink,
        "status_code": 200
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    endpoint.run(host='0.0.0.0', port=9000)
