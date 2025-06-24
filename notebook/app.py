from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load('model1.pkl')
preprocessor = joblib.load('preprocessor.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = {
            'carat': float(request.form['carat']),
            'cut': request.form['cut'],
            'color': request.form['color'],
            'clarity': request.form['clarity'],
            'depth': float(request.form['depth']),
            'table': float(request.form['table']),
            'x': float(request.form['x']),
            'y': float(request.form['y']),
            'z': float(request.form['z']),
        }
        
        input_data = pd.DataFrame([data])
        
        input_data = preprocessor.transform(input_data)
        
        predicted_price = model.predict(input_data)[0] 
        return jsonify({'price': round(predicted_price, 2)})  

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
