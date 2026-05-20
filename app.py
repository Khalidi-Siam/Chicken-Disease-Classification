import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from src.chicken_disease_classification.pipeline.prediction import PredictionPipeline

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})
        
    try:
        # Save the uploaded file temporarily
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
            
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)

        # Make prediction
        classifier = PredictionPipeline(filepath)
        prediction_result = classifier.predict()
        
        # Clean up the file after prediction
        if os.path.exists(filepath):
            os.remove(filepath)
            
        return jsonify(prediction_result)
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
