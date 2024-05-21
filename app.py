from flask import Flask, render_template, request, redirect, url_for, send_file
from pytube import YouTube
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        youtube_url = request.form.get('url')
        yt = YouTube(youtube_url)
        video = yt.streams.get_highest_resolution()
        video_path = video.download(output_path='./downloads')
        return send_file(video_path, as_attachment=True)
    else:
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()