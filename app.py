from flask import Flask, request,render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('irisdata.html')


@app.route('/irispredict',methods=['POST'])
def iris_predict():
    iris_features=[float(x) for x in request.form.values()]
    irismodel=pickle.load(open("irismodel.pkl",'rb'))
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

if __name__ == "__main__":
    app.run(debug=False)