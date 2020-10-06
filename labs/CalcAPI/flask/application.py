from flask import Flask,request,jsonify
from pycalc import dot_prod,get_rand_array

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "<h1>I'm alive!</h2><p>version 3.0"


@app.route('/dotprod', methods=['POST'])
def dotprod():
    injson = request.get_json()
    arr1 = injson['arr1']
    arr2 = injson['arr2']
    rval = dot_prod(arr1,arr2)
    return jsonify({"result":rval})
	

@app.route('/dotprodtest', methods=['GET'])
def dotprodTest():
    pyarr = [float(x) for x in range(1,11)]
    rval = dot_prod(pyarr,pyarr)
    return jsonify({"result":rval, "passed":rval==385.0})
    

@app.route('/random/<int:size>', methods=['GET'])
def getrandom(size):
    r_arr = get_rand_array(int(size))
    return jsonify(r_arr)
    

