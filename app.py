import os
from pytube import YouTube
from pytube.cli import on_progress
from urllib.parse import quote
from io import BytesIO
from pytube.exceptions import PytubeError
from flask import (
    Flask,
    render_template,
    request,
    Response
)

app = Flask(__name__)

@app.route("/")
def index():
    print("Request for index page received")
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    url = request.form.get("url")
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(file_extension='mp4').first()
        buffer = BytesIO()
        stream.stream_to_buffer(buffer)
        buffer.seek(0)
    except PytubeError:
        print("Error")

    clean_title = "".join(char if char.isalnum() or char in {' ', '_', '-'} else '' for char in yt.title)
    clean_title = clean_title.strip()

    return Response(
    buffer,
    headers={
        'Content-Type': 'video/mp4',
        'Content-Disposition': f'attachment; filename="{clean_title}.mp4"; filename*=UTF-8\'\'{quote(clean_title)}.mp4'
    },
)

 
if __name__ == "__main__":
    app.run()
