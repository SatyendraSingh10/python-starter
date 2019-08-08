from flask import Flask, jsonify, request
from time import sleep
import requests
app = Flask(__name__)


@app.route('/slowclusters')
def slowclusters():
    sleep(1.0)
    clusters = ["apac", "att-api", "att-enterprise", "att-hilton", "att-poc", "att-stg", "att-stg-api", "att-stg-thd", "att-thd", "central-prod2", "china-prod", "eu", "firefly", "internal2", "prod",
                "starman", "swisscom-prod-os", "swisscom-vega-os", "telefonica"]

    return jsonify(clusters), 500


@app.route('/fastclusters')
def fastclusters():
    clusters = ["apac", "att-api", "att-enterprise", "att-hilton", "att-poc", "att-stg", "att-stg-api", "att-stg-thd", "att-thd", "central-prod2", "china-prod", "eu", "firefly", "internal2", "prod",
                "starman", "swisscom-prod-os", "swisscom-vega-os", "telefonica"]
    return jsonify(clusters)


@app.route('/noclusters1')
def noclusters():
    clusters = ["apac", "att-api", "att-enterprise", "att-hilton", "att-poc", "att-stg", "att-stg-api", "att-stg-thd", "att-thd", "central-prod2", "china-prod", "eu", "firefly", "internal2", "prod",
                "starman", "swisscom-prod-os", "swisscom-vega-os", "telefonica"]

    return jsonify(clusters)


@app.route("/status", methods=["GET"])
def status():
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
