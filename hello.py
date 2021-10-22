import json
from flask import Flask
# from flask import jsonify
from google.cloud import bigquery

app = Flask(__name__)

@app.route('/')
def hi():

    value = {
        "response1": "hi",
        "response2": "hello"
    }
    return json.dumps(value)

@app.route('/prediction')
def predictionResults():
    bqclient = bigquery.Client()
    query_string = """SELECT FROM `burnished-ember-328422.census.predictionResults` LIMIT 10"""

    df = (
        bqclient.query(query_string)
        .result()
        .to_dataframe(
            # Optionally, explicitly request to use the BigQuery Storage API. As of
            # google-cloud-bigquery version 1.26.0 and above, the BigQuery Storage
            # API is used by default.
            create_bqstorage_client=True,
        )
    )
    shorten = df.head(10)
    json_results = shorten.to_json()
    return json_results

if __name__ == '__hello__':
    app.run(host='127.0.0.1', port=8080, debug=True)
