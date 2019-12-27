from flask import Flask, request, jsonify
from dotenv import dotenv_values
from contextlib import redirect_stdout
from io import StringIO
import tempfile
import os
import json
import sys
app = Flask(__name__)

@app.route('/', methods=['POST'])
def unpickling():
    # Load environment
    env_file = request.files['env_file']
    env = StringIO(env_file.read().decode('utf-8'))
    env.seek(0)
    parsed = dotenv_values(stream=env)
    for key, value in parsed.items():
        os.environ[key] = value

    # Load geofile
    geo_file = request.files['geo_file']
    temp = tempfile.NamedTemporaryFile(mode="w+b", suffix='.py', delete=True)
    temp.write(geo_file.read())
    temp.seek(0)
    os.system(f'python {temp.name}')
    return jsonify('please check database to see if it actually worked')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)