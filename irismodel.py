import pandas as pd
import pickle
import os

dataset=pd.read_csv("D:\\testapp\\Heroku-Demo\\iris.data",names=['sepal_length','sepal_width','petal_length','petal_width','class_type'])

def get_class(class_type):
    if(class_type=='Iris-setosa'):
        return 1
    if (class_type == 'Iris-versicolor'):
        return 0
    if (class_type == 'Iris-virginica'):
        return 2
dataset['class_type']=dataset['class_type'].apply(lambda x:get_class(x))

X = dataset.iloc[:, :4]
y = dataset.iloc[:, -1]

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=10)
model.fit(X,y)
if(os.path.exists("D:\\testapp\\Heroku-Demo\\irismodel.pkl")):
    os.remove("D:\\testapp\\Heroku-Demo\\irismodel.pkl")
pickle.dump(model,open('D:\\testapp\\Heroku-Demo\\irismodel.pkl','wb'))