import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('irisdata.html')


@app.route('/irispredict',methods=['POST'])
def iris_predict():
    iris_features=[float(x) for x in request.form.values()]
    irismodel=pickle.load(open("D:\\testapp\\Heroku-Demo\\irismodel.pkl",'rb'))
    prediction=irismodel.predict([iris_features])
    if(prediction[0]==2):
        class_type="Iris-virginica"
    if (prediction[0] == 0):
        class_type = "Iris-versicolor"
    if (prediction[0] == 1):
        class_type = "Iris-setosa"
    return render_template('irisdata.html',\
                           prediction_result="Class type of the flower:{} ".format(class_type),\
                           sepal_length="Sepal Length:{} ".format(iris_features[0]),\
                           sepal_width="Sepal Width:{} ".format(iris_features[1]),\
                           petal_length="Petal Length:{} ".format(iris_features[2]),\
                           petal_width="Petal Width:{} ".format(iris_features[3]))

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    for i in request.form.values():
        print(i)

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    print(final_features)
    print(type(final_features))
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)