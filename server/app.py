from flask import Flask, request
from server.core.Core import Core
from server.core.engine import *
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)

@app.route("/search", methods=['GET'])
@cross_origin()
def getProducts():
    args = request.args
    args.to_dict()
    name = args.get('name', default="", type=str)
    print("running")

    try:
        init = Core(str(name)).process()

        if init or len(init) > 1:
            res = json.dumps(init)
            return res
    except:
        raise Exception("failed to load products, please try again")
    

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
