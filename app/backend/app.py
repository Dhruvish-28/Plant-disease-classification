from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import yaml
import os
from model import PlantDiseaseClassifier

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load configuration
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Initialize model
classifier = PlantDiseaseClassifier(
    model_path=config['model']['path'],
    classes=config['model']['classes']
)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'Flask server is running'}), 200

# @app.route('/classify', methods=['POST'])
# def classify():
#     """Classify a plant disease from an uploaded image"""
#     try:
#         # Check if image is in request
#         if 'image' not in request.files:
#             return jsonify({'error': 'No image provided'}), 400
        
#         file = request.files['image']
        
#         if file.filename == '':
#             return jsonify({'error': 'No file selected'}), 400
        
#         if not allowed_file(file.filename):
#             return jsonify({'error': 'Invalid file format. Allowed: png, jpg, jpeg, gif'}), 400
        
#         # Save temporary file
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)
        
#         # Classify the image
#         result = classifier.classify(filepath)
        
#         # Clean up
#         os.remove(filepath)
        
#         return jsonify(result), 200
    
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

@app.route('/classify', methods=['POST'])
def classify():
    """Classify a plant disease from an uploaded image"""
    try:

        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']

        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file format. Allowed: png, jpg, jpeg'}), 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        file.save(filepath)

        result = classifier.classify(filepath)

        os.remove(filepath)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/config', methods=['GET'])
def get_config():
    """Get application configuration (classes, etc.)"""
    return jsonify({
        'classes': config['model']['classes'],
        'description': config.get('description', '')
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
