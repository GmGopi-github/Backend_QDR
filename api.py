import os
from flask import Flask,request
import json 
from flask_cors import CORS
import base64
import onnx

app = Flask(__name__)
cors = CORS(app)

datasetPath = 'data'

@app.route('/api/upload_canvas', methods=['POST'])
def upload_canvas():
    data = json.loads(request.data.decode('utf-8'))
    image = data['image'].split(',')[1].encode('utf-8')
    fileName = data['filename']
    className = data['classname']
    os.makedirs(f'{datasetPath}/{className}/image', exist_ok=True)
    with open(f'{datasetPath}/{className}/image/{fileName}', 'wb') as fh:
        fh.write(base64.decodebytes(image))

    return "got the image"

@app.route('/api/result', methods=['POST'])
def result():
    data = json.loads(request.data.decode('utf-8'))
    image = data['image'].split(',')[1].encode('utf-8')
    fileName = data['filename']
    os.makedirs(f'playgamedata/image', exist_ok=True)
    with open(f'playgamedata/image/{fileName}', 'wb') as fh:
        fh.write(base64.decodebytes(image))

    return onnx.test('playgamedata/image/'+fileName)