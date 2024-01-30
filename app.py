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
    send_from_directory,
    Response
)

app = Flask(__name__)

@app.route("/")
def index():
    print("Request for index page received")
    return render_template("index.html")

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )

@app.route("/hello", methods=["POST"])
def hello():
    url = request.form.get("url")
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        buffer = BytesIO()
        
        # Getting the highest resolution
        video = yt.streams.filter(only_audio=False).order_by("resolution").desc().first()
        
        # Download the video
        video.stream_to_buffer(buffer)
        buffer.seek(0)
    except PytubeError:
        print("Error")

    # Clean up the video title
    clean_title = "".join(char if char.isalnum() or char in {' ', '_', '-'} else '' for char in video.title)
    clean_title = clean_title.strip()

    return Response(
        buffer,
        headers={
            'Content-Type': 'video/mp4',
            'Content-Disposition': f'attachment; filename={quote(clean_title)}.mp4',
        },
    )

if __name__ == "__main__":
    app.run()