import joblib

class Model:
    def __init__(self):
        self.model = joblib.load('model/best_model.pkl')

    def predict(self, input_features):
        return self.model.predict(input_features)
    
    def predict_proba(self, input_features):
        return self.model.predict_proba(input_features)

class LabelEncoder:
    def __init__(self):
        self.encoders = joblib.load('model/label_encoders.pkl')
    
    def transform(self, data):
        encoded_data = {}
        for feature, value in data.items():
            if feature in self.encoders:
                encoded_data[feature] = self.encoders[feature].transform([value])[0]
            else:
                encoded_data[feature] = value
        return encoded_data