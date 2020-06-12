import flask
from flask import request
app = flask.Flask(__name__)

from flask_cors import CORS
CORS(app)

@app.route('/')
def default():
    return '<h1> API Server is working </h1>'

@app.route('/predict')
def predict():
    from sklearn.externals import joblib
    model = joblib.load('marriage_age_predict_model.ml')
    predicted_age_of_marriage = model.predict([[int(request.args['gender']),
                                  int(request.args['religion']),
                                  int(request.args['caste']),
                                  int(request.args['mother_tongue']),
                                  int(request.args['country']),
                                  int(request.args['height_cms'])
    
    
    ]])
    return str(round(predicted_age_of_marriage[0],2))

if __name__ == "__main__":
    app.run(debug=True)