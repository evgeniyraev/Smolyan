from flask import Flask, request, jsonify, render_template
import os
from mockMottor import *

app = Flask(__name__)

@app.route('/')
def index():
    print("get index")
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_endpont():
    direction = request.form.get('direction')
    if direction == 'clockwise':
        cw()
    elif direction == 'counterclockwise':
        ccw()

    return jsonify({'status': 'success'})

@app.route('/stop', methods=['POST'])
def stop_endpoint():
    stop_rotation()
    return jsonify({'status': 'success'})

@app.route('/position', methods=['GET', 'POST'])
def position_endpoint():
    global current_position
    if request.method == 'POST':
        position = request.json.get('position')
        current_position = position
        return jsonify({'status': 'success'})
    else:
        return jsonify({"position": current_position})

@app.route('/speed', methods=['GET', 'POST'])
def set_speed():
    global current_speed
    if request.method == 'POST':
        speed = request.json.get('speed')
        with open('speed.txt', 'w') as f:
            f.write(str(speed))
        current_speed = speed
        return jsonify({'status': 'success'})
    else:
        return jsonify({"speed":current_speed})

def start_web_intergace():
    listen()
    app.run(host="0.0.0.0", port=80, debug=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)


