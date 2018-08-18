from flask import Flask
import pickle
import numpy as np

tree = pickle.load(open('Decision_Tree', 'rb'))

app = Flask(__name__)

@app.route('/')
def example():
    return '''
    <h1>
    Russian house market. 
    
    Please enter house params, 
    
    for example /full_sq=40.0/raion_popul=150000/shopping_centers_km=0.5</h1>
    '''

@app.route('/full_sq=<float:full_sq>/raion_popul=<int:raion_popul>/shopping_centers_km=<float:shopping_centers_km>')
def predict(full_sq, raion_popul, shopping_centers_km):
    p = np.floor(tree.predict(np.array([[full_sq, raion_popul, shopping_centers_km]])))[0]
    return '<h1>House price is %d</h1>' %p



import os

port = int(os.environ["PORT"])
app.run(port=port, host='0.0.0.0')
