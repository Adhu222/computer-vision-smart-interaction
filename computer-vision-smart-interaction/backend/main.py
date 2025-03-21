from flask import Flask, request, jsonify, send_file
import os
from object_detection import detect_objects

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    output_path = detect_objects(filepath)
    return send_file(output_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
