import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
#loading model
model = pickle.load(open('model.pkl', 'rb'))
#class_labels for target variable engine rating
class_labels = {5.0 : 1, 4.5 : 2, 4.0 : 3, 3.5 : 4, 3.0 : 5, 2.5 : 6, 2.0 : 7,
                1.5 : 8, 1.0 : 9, 0.5 : 10}


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    #print(data)
    prediction = model.predict([np.array(list(data.values()))])

    output = int(prediction[0])
    output = [class_ for class_,label in class_labels.items() if label == output][0]
    #print(prediction)
    #return
    return {'output' : output, 'data' : data, 'values' : list(data.values())}

if __name__ == "__main__":
    app.run(debug=True)