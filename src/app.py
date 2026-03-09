from flask import Flask, jsonify, request
import os
from flask_cors import CORS

from inference import predict_image

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/classify', methods=["POST"])
def classify():

    try:
        file = request.files["image"]

        image_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(image_path)

        predictions = predict_image(image_path)

        os.remove(image_path)
        
        top_class = predictions[0][0]
        top_conf = predictions[0][1]
        
        top3 = []

        for cls, prob in predictions[:3]:
            top3.append({
                "disease": cls.replace("___"," ").replace("_"," "),
                "confidence": round(prob * 100, 2)
            })

        return jsonify({
            "disease": top_class.replace("___"," ").replace("_"," "),
            "confidence_percentage": round(top_conf,2),
            "top_predictions": top3
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
