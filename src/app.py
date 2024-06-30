from flask import Flask, request, render_template
from model import Model
from model import LabelEncoder
import numpy as np

app = Flask(__name__)

model = Model()
label_encoders = LabelEncoder()

# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)
        # print(form_input)

        encoded_inputs = label_encoders.transform(form_input)
        
        model_inputs = np.array(list(encoded_inputs.values()), dtype=float).reshape(1, -1)

        prediction = model.predict(model_inputs)
        
        prediction_label = 'customer will churn' if prediction[0] == 1 else 'customer will not churn'
        
        prediction_proba = model.predict_proba(model_inputs)[0][1]
        prediction_proba = f"{prediction_proba:.4f}"

        return render_template('index.html', prediction_label=prediction_label, prediction_proba=prediction_proba)

    return render_template('index.html')


# # Method 2: Via POST API
# @app.route('/api/predict', methods=['POST'])
# def predict():
#     request_data = request.get_json()
#     print(request_data)

#     return {'success': False}, 500


if __name__ == '__main__':
    app.run(debug=True)
