#!/usr/bin/python3

import json

from flask import Flask
from flask import render_template, request, url_for, Response
import downloader.ytdl as ytdl

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view', methods=['GET'])
def view():
    url = request.args.get('url', '')
    print(url)
    # return ytdl.getResult(url)
    result = ytdl.getResult(url)
    if ytdl.isPlaylist(result):
        #playlists are not supported yet
        print("Playlist detected. Returning the first item.")
        result = result['entries'][0]

    return Response(json.dumps(result), mimetype='application/json')

if __name__ == "__main__":
    app.run()