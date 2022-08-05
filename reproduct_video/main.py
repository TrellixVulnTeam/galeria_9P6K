from flask import Flask, request
from view import Manager
from flask import render_template, send_file
import os
import io

app = Flask(__name__, template_folder='template')

@app.route('/playvideo', methods=['GET'])
def play_video():
    args = request.args
    if args and "video" in args:
        path_video = Manager().video_path(int(args["video"]))
        return render_template("index.html", path_video=path_video)

@app.route('/playimage', methods=['GET'])
def play_image():
    args = request.args
    if args and "image" in args:
        path_image = Manager().image_path(int(args["image"]))
        return render_template("index_image.html", path_image=path_image)


@app.route('/movie_day.mp4')
def video_file_day():
    video_path = "/etc/galeria/media/movie_day.mp4"
    return send_file(io.BytesIO(open(video_path, "rb").read()), mimetype='video/mp4')

@app.route('/movie_night.mp4')
def video_file_night():
    video_path = "/etc/galeria/media/movie_night.mp4"
    return send_file(io.BytesIO(open(video_path, "rb").read()), mimetype='video/mp4')

@app.route('/parking_full.jpg')
def image_file_parking_full():
    image_path = "/etc/galeria/media/parking_full.jpg"
    return send_file(io.BytesIO(open(image_path, "rb").read()), mimetype='image/jpg')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)
