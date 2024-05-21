from flask import Flask, render_template, request, redirect, url_for, send_file
from pytube import YouTube
from io import BytesIO


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

        # Stream the video directly to the client without saving to disk
        video_stream = BytesIO()
        video_stream.write(video.stream_to_buffer())
        video_stream.seek(0)

        # Set Content-Disposition header to force download
        return send_file(video_stream, attachment_filename=f"{yt.title}.mp4", as_attachment=True)

if __name__ == "__main__":
    app.run()