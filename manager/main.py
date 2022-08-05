from flask import Flask, request
from view import ManageConfig, ManageApplication
from flask_cors import CORS
from flask import render_template, send_file
import io

app = Flask(__name__, template_folder='template')
CORS(app)

@app.route('/configuration', methods=['GET'])
def get_config():
    return ManageConfig().get_config()

@app.route('/saveconfiguration', methods=['POST'])
def post_config():
    return ManageConfig().save_config(request)

@app.route('/playimage', methods=['get'])
def set_image():
    return ManageApplication.set_image()

@app.route('/playvideo', methods=['get'])
def set_video():
    return ManageApplication.set_video()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)