from flask import Flask, request, render_template, jsonify
from server.core.Core import Core
from server.core.Algo import Algo
from server.core.engine import *
from flask_cors import CORS, cross_origin
from server.db import create_table_if_not_exists, create_connection
import time
import logging
import json
from server.core.text_preprocessor import sanitize_text

app = Flask(__name__)
cors = CORS(app)
logger = logging.getLogger(__name__)


def start_timer():
    request.start_time = time.time()


def end_timer():
    end_time = time.time()
    response_time = end_time - request.start_time
    app.logger.info(
        f"Request to {request.path} took {response_time:.4f} seconds")
    print(f"Request to {request.path} took {response_time:.4f} seconds")


@app.route("/", methods={'GET'})
def render_home():
    create_table_if_not_exists()
    url = request.host_url
    return render_template("index.html", url=url)


@app.route("/search", methods=['GET'])
@cross_origin()
def getProducts():
    args = request.args
    args.to_dict()
    name = args.get('name', default="", type=str)
    start_timer()
    print("running")

    try:

        # get the data from db
        # create an algo class and pass in the core process and the db link
        # create a method to parse both of them together and sort by number of clicks
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM product_metadata")
        metadata = cursor.fetchall()

        title_click_dict = {}

        for item in metadata:
            title, click = item[1], item[2]
            title_click_dict[title] = click

        connection.commit()
        cursor.close()
        connection.close()
        pre_process_name = sanitize_text(name)
        init = Core(str(pre_process_name)).getProducts()
        rank = Algo(init, title_click_dict).rank_data()
        # print("rank data ", rank)

        if rank and init or len(rank) > 1:
            res = json.dumps(rank)
            end_timer()
            return res
    except:
        raise Exception("failed to load products, please try again")


@app.route("/update", methods=['POST'])
@cross_origin()
def update_metadata():
    print("data running")
    print(f"data request {request.get_json()}")
    try:
        data = request.get_json()
        print(f"data {data}")

        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT clicks FROM product_metadata WHERE name = %s;", (data['title'],))
        existing_elem = cursor.fetchone()

        if existing_elem:
            updated_clicks = existing_elem[0] + 1
            cursor.execute(
                "UPDATE product_metadata SET clicks = %s WHERE name = %s;", (updated_clicks, data['title']))
        else:
            cursor.execute(
                "INSERT INTO product_metadata (name, clicks) VALUES (%s, %s);", (data['title'], 1))

        connection.commit()
        cursor.close()
        connection.close()
        return {"status": True}
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    # app.run(debug=False, host='0.0.0.')
    create_table_if_not_exists()
    app.run(debug=True, host='0.0.0.')
